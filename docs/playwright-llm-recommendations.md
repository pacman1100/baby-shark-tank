# Best local LLMs for Playwright-style agent automation

## Corrections to the earlier note

- **`codellama:34b` is likely not installed yet.** The earlier Ollama list you shared had several 7–20B class models but did not include `codellama:34b`. It exists in Ollama’s library, but it must be pulled separately.
- **Newer code specialists outperform CodeLlama 34B for Playwright agents.** Qwen2.5-Coder and DeepSeek-Coder-V2 variants tend to do better on instruction following and tool/action formatting.

## Best local LLMs for Playwright-style agent automation (today)

### Tier A (recommended first)

- **Qwen2.5-Coder (7B/14B/32B)** — strong code reasoning + code fixing; very usable via Ollama, and the 7B is a great “always-on” runner.
- **DeepSeek-Coder-V2:lite** — excellent for coding/tool-use patterns; great when you want reliable step-by-step generation.

### Tier B (good, but situational)

- **CodeLlama 34B** — still solid, but heavier/slower locally unless you’re OK with aggressive quantization and CPU/RAM offload.
- **Llama 3 8B / Llama 3.x 8B** — decent generalist; workable if you enforce JSON strictly on the runner side, but less “code-native” than the two above.

## Practical recommendation for an RTX 3080-class setup

1. **Default model:** `qwen2.5-coder:7b` (fast, good structured outputs)
2. **“Hard tasks” model:** `deepseek-coder-v2:lite` (better on complex refactors / multi-step)
3. Only then consider `codellama:34b` if you specifically prefer its style.

## References (copy/paste)

```text
https://ollama.com/library/qwen2.5-coder
https://ollama.com/library/deepseek-coder-v2:lite
https://ollama.com/library/codellama:34b
https://playwright.dev/python/docs/api/class-page
```

**Confidence:** High (0.86) on the model picks; Medium (0.63) on the “you don’t currently have codellama:34b installed” detail unless you confirm with `ollama list`.
