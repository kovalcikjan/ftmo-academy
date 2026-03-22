"""Text generation via external LLM APIs for FTMO Academy workflow.

Called by Claude Code when user selects an external model for content generation.
Reads a system prompt + input content, sends to selected model, writes output.

Usage:
    python src/generate_text.py --model gpt-4o --system prompts/step2_tov.md --input article.md --output result.md
    python src/generate_text.py --list  # show available models + API key status
"""

import argparse
import sys
from pathlib import Path

from adapters import ClaudeAdapter, GeminiAdapter, OpenAIAdapter
from adapters.base import BaseAdapter
from config import Config


def list_models(cfg: Config) -> None:
    """Print available models and API key status."""
    api_status = cfg.validate()
    print("Available models:\n")
    print(f"  {'Model':<25} {'Provider':<12} {'API Key'}")
    print(f"  {'-'*25} {'-'*12} {'-'*10}")
    for key, model in cfg.models.items():
        status = "OK" if api_status.get(model.provider) else "MISSING"
        print(f"  {key:<25} {model.provider:<12} {status}")


def get_adapter(model_name: str, cfg: Config) -> BaseAdapter:
    """Get initialized adapter for a model.

    Args:
        model_name: Model key from config (e.g. 'gpt-4o').
        cfg: Application configuration.

    Returns:
        Initialized adapter ready to call.

    Raises:
        ValueError: If model or provider is unknown or API key missing.
    """
    if model_name not in cfg.models:
        available = ", ".join(cfg.models.keys())
        raise ValueError(f"Unknown model: {model_name}. Available: {available}")

    model_config = cfg.models[model_name]
    api_key = cfg.get_api_key(model_config.provider)

    adapters: dict[str, type[BaseAdapter]] = {
        "openai": OpenAIAdapter,
        "google": GeminiAdapter,
        "anthropic": ClaudeAdapter,
    }

    adapter_class = adapters.get(model_config.provider)
    if not adapter_class:
        raise ValueError(f"Unknown provider: {model_config.provider}")

    return adapter_class(api_key, model_config.model_id)


def generate(
    model_name: str,
    system_prompt_path: Path,
    input_path: Path,
    output_path: Path,
    max_tokens: int = 8192,
    temperature: float = 0.7,
) -> None:
    """Generate text using an external LLM.

    Args:
        model_name: Model key from config.
        system_prompt_path: Path to system prompt markdown file.
        input_path: Path to input content file.
        output_path: Path to write generated output.
        max_tokens: Maximum tokens in response.
        temperature: Sampling temperature.
    """
    cfg = Config()
    adapter = get_adapter(model_name, cfg)
    model_config = cfg.models[model_name]

    system_prompt = system_prompt_path.read_text(encoding="utf-8")
    input_content = input_path.read_text(encoding="utf-8")

    print(f"Model: {model_config.name} ({model_config.model_id})")
    print(f"Provider: {model_config.provider}")
    print(f"System prompt: {system_prompt_path.name} ({len(system_prompt)} chars)")
    print(f"Input: {input_path.name} ({len(input_content)} chars)")
    print("Generating...")

    response = adapter.call(
        system_prompt=system_prompt,
        user_message=input_content,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(response.content, encoding="utf-8")

    print(f"Output: {output_path} ({len(response.content)} chars)")
    print(f"Tokens: {response.input_tokens} in / {response.output_tokens} out / {response.total_tokens} total")


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate text via external LLM for FTMO Academy workflow.",
    )
    parser.add_argument("--list", action="store_true", help="List available models")
    parser.add_argument("--model", type=str, help="Model to use (e.g. gpt-4o)")
    parser.add_argument("--system", type=str, help="Path to system prompt file")
    parser.add_argument("--input", type=str, help="Path to input content file")
    parser.add_argument("--output", type=str, help="Path to write output")
    parser.add_argument("--max-tokens", type=int, default=8192, help="Max output tokens")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature")

    args = parser.parse_args()

    if args.list:
        list_models(Config())
        return

    if not all([args.model, args.system, args.input, args.output]):
        parser.error("--model, --system, --input, and --output are required")

    generate(
        model_name=args.model,
        system_prompt_path=Path(args.system),
        input_path=Path(args.input),
        output_path=Path(args.output),
        max_tokens=args.max_tokens,
        temperature=args.temperature,
    )


if __name__ == "__main__":
    main()
