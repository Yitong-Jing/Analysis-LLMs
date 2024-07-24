# Berechnung Perplexity mit GPT-2
import LLMs_json_input.Openassistant_automatisch as generierterText_LLM
import evaluate


# Load some sentences
generierterTexte = generierterText_LLM.antwort

perplexity = evaluate.load("perplexity", module_type="metric")
results = perplexity.compute(model_id='gpt2',
                             add_start_token=False,
                             predictions=generierterTexte)
print(round(results["mean_perplexity"], 2))

