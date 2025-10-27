import os
import csv
import pandas as pd
# from torch import nn
# from transformers.models.llama.modeling_llama import *
# from transformers import (AutoTokenizer, AutoConfig, LlamaForCausalLM, DataCollatorForLanguageModeling, Trainer, TrainingArguments)
# from datasets import load_dataset
from huggingface_hub import login
#import wandb
from tqdm import tqdm

# WANDB_TOKEN = "b6fadc8759afd5bdc289a61679958dfa95e3e0a3"
#HF_TOKEN = "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"
#Puth the HF tokem
HF_TOKEN = ""

# wandb.login(key=WANDB_TOKEN)
login(token=HF_TOKEN)

# df = pd.DataFrame()

d = {
    "text_comprehension.csv": '''
Instruction: You are given a passage followed by a question. Read the passage carefully and analyze the information provided. Answer the question based solely on the information from the passage. Your response should be clear, concise, and supported by evidence from the passage.

Input: Passage: Oral phenobarbital has been used in rwninants at 11 mg/kg/day and in horses at 3---11 mg/kg/day. Senun concentrations should be checked periodically. The elimination half-life is extremely long (24 days) in dogs; therefore, it takes -4 mo to achieve steady state kinetics. Bromide is renally eliminated and thus should not be used in dogs with renal dysfunction without careful monitoring. lf azotemia is present, a different AED can be used, or the initial bromide dose can be reduced by half and serwn concentrations monitored. Because it does not undergo hepatic metabolism, bromide is useful in dogs with liver disease. As adjunct therapy with phenobarbital, potassium bromide can be administered at 20-40 mg/kg/day, PO, either as one dose or divided into two or more doses; the sodiwn bromide dosage is slightly lower at 17-30 mg/kg/day, PO. When bromide is used as the sole treatment for epilepsy in dogs, higher dosages (50-80 mg/kg/day) may be necessary. Dogs on a high salt diet may require dosages of 50-80 mg/kg/day to maintain adequate senun concentrations, because high chloride intake increases bromide loss in the urine and lowers senun bromide concentrations. Many laboratory assays carmot distinguish between sernm bromide and chloride ions, so serum chloride values may be rep01ted as falsely high. Because a daily maintenance dose may take 4 mo to reach steady state serum concentration, there are situations ( eg, severe seizures, seizures that occur on a monthly basis, the need to rapidly switch from phenobarbital to bromide because of phenobarbital toxicity) when a loading dose of bromide should be administered loading dosage of 400-600 mg/kg of bromide is divided into four doses and given with food over a 1to 4-day period. Smaller doses, such as 50 mg/kg, bid for 4-6 days, may reduce adverse effects ( eg, nausea and vomiting) caused by rapid increase in serum bromide concentrations. The regular maintenance dose can be started at the same tin1e as the loading dose or immedi ately afterward. The loading dose regimen can be discontinued if the dog becomes too sedated, or smaller divided daily doses can be tried. A serwn sample can be submitted within 2 wk after loading to detem1ine whether a therapeutic level has been reached. (lf cost is an issue, however, a sample is best checked in 4 mo when steady-state concentrations have been reached.) The therapeutic range for bromide is 1-2 mg/mL (10-20 mmol/L) with concuffent phenobarbital treatment, or 1-3 mg/mL (10-30 mmol/L) for bromide as a monotherapy. However, the dosing regimen needs to be tailored for each animal; the upper end of the therapeutic range is only limited by adverse effects of bromide. Bromide is generally well tolerated by dogs, but potential adverse effects include bitter taste, gastric irritation, nausea (particularly with the potassiwn form), polywia, polydipsia, polyphagia, sedation, ataxia, and pancreatitis. It should be administered with food; the amount and type of food given should be kept constant, because variable dietary salt content will affect the elin1ination of bromide via the kidneys. Bromide tl1erapy must be titrated to the individual anin1al based on careful therapeutic drug monitoring and careful monitoring by the owner for early signs of toxicity. Reports of hindlirnb weakness should be investigated as potential bromide toxicosis by measuring serum bromide concentration and discontinuing bromide for several days to see whether the weakness improves. Severe bromide toxicosis (bromism) is characterized by lethar*gy, disorientation, delliiwn, and ataxia progressing to quadriplegia and coma. Bromide toxicity can be seen at any concentration in an unusually sensitive dog, but it is rar*e when bromide is used alone and when serum concentrations are <1.5 mg/mL (15 mmol/L). When used in combination with phenobarbital, bromide toxicity car1 be seen at concentrations of 2-3 mg/mL (20-30 nunol/L). Severe signs of toxicity are easily treated by IV adn1inistration of 0.99(, sodiun1 chloride, which promotes renal excretion of the bromide ion. Bromide is an effective maintenance AED in cats, but the incidence of adverse effects 
Question: What are the primary considerations for dosing potassium bromide in dogs, including in cases of renal dysfunction or high salt diets?
Based on the passage, provide an answer to the question. Use evidence from the passage to support your answer. 

Output: Answer: The primary considerations for dosing potassium bromide in dogs include monitoring serum concentrations periodically, especially in cases of renal dysfunction, where bromide should be used with careful monitoring or a reduced initial dose. For dogs on high salt diets, dosages of 50-80 mg/kg/day may be required to maintain adequate serum concentrations due to increased bromide loss in urine. Serum bromide and chloride ion levels need to be accurately monitored as many laboratory assays cannot distinguish between the two, potentially leading to falsely high serum chloride values.


Instruction: You are given a passage followed by a question. Read the passage carefully and analyze the information provided. Answer the question based solely on the information from the passage. Your response should be clear, concise, and supported by evidence from the passage.

Input: Passage: Toxocara cati Also known as: Toxocara mystax   Introduction  Toxocara cati is a nematode of the superfamily Ascaridoidea. T. cati is found worldwide, and can cause a wide range of gastrointestinal problems in infected hosts. There is a zoonotic risk with ingestion of larvated eggs, which can produce the conditions of visceral larval migrans and ocular larval migrans in humans. However T. canis is the more common culprit.   Hosts  Cat   Identification  T. catis is a large white worm. The female is capable of growing up to 10cm in length. The male, similar to Toxocara canis, has a finger-like process on the tip of the tail. The eggs are approximately 70mm, have no distinct colour, but have a thick, pitted outer shell.   Life Cycle  The adult worms live in the small intestine and the females produce eggs that are passed in the faeces of the cat. Infection occurs by ingestion of the L2 in the egg, or after ingestion of a paratenic host, or via transmammary route. After direct ingestion of the larvae, they migrate through the liver, lungs and trachea, and then go back to the small intestine, where they transform into L3. Ingestion of a paratenic host like a mouse causes the larvae to be released by digestion, and they then enter the small intestine of the cat, and will moult into L3. Transmammary infection is also very important, and commonly seen throughout lactation. However, unlike T. canis, prenatal infection does not occur. The prepatent period of T. catis is 8 weeks.   Clinical Signs  Infected kittens will present with stunted growth and a loss of condition. Their coat may be dull and they may appear 'pot-bellied'. Worms may be seen in vomitus or in the faeces. Migrating larvae can cause damage to internal organs leading to pneumonia and coughing, ascites, fatty liver.   Diagnosis  Infection is diagnosed by finding eggs in the faeces of the animal, using faecal flotation methods. Toxocara leonida eggs may confuse the diagnosis, but they are smooth-shelled and more oval in shape.   
Question: How can Toxocara cati infections be clinically identified in affected kittens, and what are the main clinical signs observed?
Based on the passage, provide an answer to the question. Use evidence from the passage to support your answer. 

Output: Answer: Toxocara cati infections in kittens can be clinically identified by finding eggs in the faeces through faecal flotation methods. The main clinical signs observed in infected kittens include stunted growth, loss of condition, a dull coat, and a 'pot-bellied' appearance. Worms may also be seen in vomitus or faeces. Migrating larvae can cause damage to internal organs, leading to pneumonia, coughing, ascites, and fatty liver.


Instruction: You are given a passage followed by a question. Read the passage carefully and analyze the information provided. Answer the question based solely on the information from the passage. Your response should be clear, concise, and supported by evidence from the passage.

Input: Passage: Chinchillas range from 9-15"  long with a tail of 3-10" (7.5-25 cm), and weigh from 1 to 2 lb . Their thick, shiny fur is about 1" long; the most common color of chinchillas is blue-grey. The softness of the fur is due to the fewer number of guard hairs as compared with those of fur-bearing animals. Sex identification is through anogenital distance, which is much longer in males than in females. Specifics of anatomy and other information about chinchillas can be found in the Manual of Exotic Pet Practice, pp 474-492. Chinchillas require a relatively large enclosure with specific areas for eating, sleeping, exercising, and urinating / defecating. Chinchillas live in groups in the wild and benefit from housing with at least one other chinchilla. Cages should be made of metal and wire; plastic and wood will be quickly chewed through. Hay and straw should not be used as they may become moldy or stain fur. Temperature should be kept at less than 80degF and humidity at a comfortable level for humans, as chinchillas suffer heat prostration / hyperthermia if maintained in higher environmental temperatures, especially if humidity is high. Chinchillas are nocturnal in the wild but can adapt to a diurnal lifestyle as pets.  
Question: What are the key differences in the lifestyle and behavior of chinchillas in the wild compared to those kept as pets, and how can pet owners accommodate these differences?
Based on the passage, provide an answer to the question. Use evidence from the passage to support your answer. 

Output: Answer: In the wild, chinchillas are nocturnal, but they can adapt to a diurnal lifestyle when kept as pets. Pet owners can accommodate these behavioral differences by providing a stable and soothing environment that mimics their natural habitat as much as possible, including a proper enclosure setup and social companionship. Understanding their natural nocturnal behavior can help owners be more patient with their activity patterns and ensure that their pet chinchillas receive adequate enrichment and social interaction during their active periods.


Instruction: You are given a passage followed by a question. Read the passage carefully and analyze the information provided. Answer the question based solely on the information from the passage. Your response should be clear, concise, and supported by evidence from the passage.

Input: Passage: 'Determining the Age of Shark Teeth', "Identify fossilized teeth by their dark coloring. Shark teeth contain oxygen, which can react with surrounding minerals to create colors over time. Fossilized shark teeth have had at least 10,000 years for this oxidation to take effect, so they're often black, deep red, brown, grey, or another similar dark color. This varies based on the environment that the tooth has fossilized in, because different sediments contain minerals that create different colors through oxidization. Shark teeth that are found in areas that contain iron oxide, such as parts of New Jersey, tend to have an orange or red coloring. Shark teeth found in areas that contain a lot of phosphate, such as Venice Beach, Florida, tend to be black, as phosphate is a dense, black mineral.", "Identify modern teeth by their lighter color. Modern teeth haven't yet been exposed to the minerals in surrounding sediments for the 10,000 years that it takes to cause oxidation. As a result, these teeth are typically white, and usually appear much like they did when they were in the mouth of the shark they came from.", "Find out the species and see if it's extinct. Try determining the general age of the tooth by observing its anatomy and finding out what kind of species it came from. While many shark teeth that you may find can come from sharks like tiger sharks and great white sharks that exist today, you could find one that comes from an extinct species. If you notice that the anatomy of a tooth matches that of an extinct species, the tooth is extremely old. The megalolamna paradoxodon is one example of an extinct shark species that you could possibly find the teeth of..", "Recognize teeth that are found inland as old. While you can certainly find fossilized shark teeth at the beach, both modern and fossilized teeth are frequently found in this location. If you find a tooth significantly inland, then there's a high chance that it's very old because it would take a long time for the tooth to be moved far away from the ocean by the elements. For instance, if you find a shark tooth in a creek that's 50 miles (80.5 kilometers) inland, it's probably a fossilized tooth." 
Question: What causes the dark coloring in fossilized shark teeth, and how does the environment affect this?
Based on the passage, provide an answer to the question. Use evidence from the passage to support your answer. 

Output: Answer: The dark coloring in fossilized shark teeth is caused by oxidation reactions between the oxygen in the teeth and the surrounding minerals over at least 10,000 years. The specific color varies based on the environment and the types of sediments and minerals present. For example, teeth found in areas with iron oxide, like parts of New Jersey, tend to be orange or red, while those found in phosphate-rich areas, like Venice Beach, Florida, are typically black.

According to above given examples, do same for following based on animal science:

''',
    "mcq_correct_option.csv": '''Instruction: A question is given followed by a set of options. Analyze the question and options carefully to determine the correct answer. Choose the option that best aligns with the question's context.

Input: Question: Which among the following is a C16 monounsaturated fatty acid? 
Option A: Oleic acid 
Option B: Linoleic acid 
Option C: Linolenic acid 
Option D: Palmitoleic acid

Output: Correct Option: A: Oleic acid


Instruction: A question is given followed by a set of options. Analyze the question and options carefully to determine the correct answer. Choose the option that best aligns with the question's context.

Input: Question: In the post-mortem, Brick red mucosal membrane of GI tract lesion seen in 
Option A: a) Lead poisoning 
Option B: b) Copper poisoning 
Option C: c) Mercury poisoning 
Option D: d) Arsenic poisoning

Output: Correct Option: A: a) Lead poisoning


Instruction: A question is given followed by a set of options. Analyze the question and options carefully to determine the correct answer. Choose the option that best aligns with the question's context.

Input: Question: The principal disorders of domestic ruminants in which hypoglycemia is a salient feature 
Option A: Bovine ketosis 
Option B: Ovine pregnancy toxemia 
Option C: Diabetes mellitus 
Option D: Both a and b

Output: Correct Option: D: Both a and b


Instruction: A question is given followed by a set of options. Analyze the question and options carefully to determine the correct answer. Choose the option that best aligns with the question's context.

Input: Question: Heparin acts as an anticoagulant by acting along 
Option A: Antithrombin III 
Option B: Factor III 
Option C: Factor XIII 
Option D: Factor I

Output: Correct Option: A: Antithrombin III


Instruction: A question is given followed by a set of options. Analyze the question and options carefully to determine the correct answer. Choose the option that best aligns with the question's context.

Input: Question: Malicious poisoning and doping is punished under 
Option A: IPC 428 & 429 
Option B: IPC 420 
Option C: IPC 415 
Option D: IPC 430

Output: Correct Option: A: IPC 428 & 429


According to above given examples, do same for following based on animal science:
''',
    "summarization.csv": '''Instruction: Summarize following passage

Input: Pig production faces seasonal fluctuations, especially during summer heat stress (HS). HS leads to low farrowing rates of breeding sows during the summer. Based on prior studies, hot season reduces sperm motility and concentration in boars, resulting in lower farrowing rates in summer mating sows. Sows that mate in the summer are also more prone to early pregnancy abortion than those that mate in other seasons. HS increases carcass fat in the offspring of sows bred in the summer by reducing fetal muscle fiber development during pregnancy. HS reduces feed intake and the growth rates of pigs in the summer and leads to a reduction in milk production in lactating sows. These three adverse effects induced by HS are identified as important factors that affect the pig industry.  Mannose oligosaccharide (MOS) is a functional oligosaccharide derived from the outer layer of the yeast cell wall and is considered as an alternative to antibiotics in animal production. As a recognized prebiotic, MOS can reduce the adverse effects of HS on animals. Supplementing 1 g/kg MOS in broiler diets for 42 days reduced serum tumor necrosis factor alpha (TNF-α) content, liver Toll-like receptor 4 (TLR4), and TNF-α mRNA abundance under HS conditions (32–33°C). Previously, Liu revealed that under HS conditions, dietary supplementation with 0.8 ppm Se, 1% yeast nucleotides, and 0.1% MOS significantly reduced sow body weight loss (p=0.037). Supplementation of MOS at 250 mg/kg in the diet was effective in improving broiler growth performance (ADG, ADFI and feed conversion ratio). Supplementing MOS in the diet improved the quality of colostrum, and promoted piglet growth performance and innate immunity in lactating and nursery piglets. The increase in ADG was due to the promotion of MOS on nutrient digestibility, gut microbiology, and barrier integrity, oxidative state and animal immunity. He et al. showed that gut microbiota composition responding to HS could be considered as biomarkers in monogastric animals. MOS promotes the growth of beneficial bacteria in the digestive tract of animals and suppresses the growth of pathogenic bacteria. Beneficial intestinal bacteria, such as Lactobacillus and Bifidobacterium, utilize MOS to produce short chain fatty acids (SCFA) and lactic acid (LA), reduce the pH value in the intestine and prevent pathogens, such as Escherichia coli and Clostridium perfringens, from adhering to the intestinal mucosa.  Studies have shown that 12 hours of HS can induce an inflammatory response in porcine skeletal muscle. Diet supplemented with MOS may contribute to the maintenance of intestinal integrity and nutrient digestion and absorption in the intestine after weaning. As an immune regulator and prebiotic, MOS may alleviate the adverse reactions under HS by improving the gut microbiota and nutrient absorption of pigs.  Extensive studies have demonstrated that dietary supplementation with MOS could improve growth performance, enhance the immune ability of intestinal mucosa, and inhibit the intestinal and systemic inflammatory response of weaned piglets. In an HS environment, dietary MOS supplementation improved inflammatory response in broiler liver and improved their growth performance, oxidation state, and integrity of the intestinal barrier. Most studies on MOS in animals under HS conditions have been performed with broilers. Thus, studies on the regulatory effect of MOS in sows in an HS environment are limited. The present study sought to explore the effects of supplementing diets with MOS on the reproductive performance and lactation performance of sows to establish a theoretical basis for reducing the adverse reactions of sows under an HS environment and reduce the economic losses in the pig industry during HS conditions.

Output: The aim of this study was to determine the effects of dietary supplementation with mannose oligosaccharide (MOS) on the condition of the body and the reproductive and lactation performances of sows. Eighty pregnant sows were randomly assigned to four groups with a 2×2 factorial design: with or without MOS (1 g/kg) and with or without heat stress (HS) challenge. The temperature in the HS groups (HS and HM group) was controlled at 31.56±1.22°C, while the temperature in the active cooling (AC) groups (AC and AM group) was controlled at 23.49±0.72°C. The weight loss of sows in the AC group was significantly lower than that of sows in the HS group (p<0.01). The weight and backfat thickness loss of sows supplemented with MOS displayed a downward trend. The average birth weight of the litter significantly increased in the HM group (basic diet + MOS) compared with the HS group (p<0.05). The milk protein of sows significantly decreased under the HS condition at 2 and 12 hours after delivery (p<0.05). However, the milk immunoglobulin G (IgG) of sows in the HS group increased significantly compared with that of sows in the HM group (p<0.05) at 12 and 24 hours after delivery. The levels of serum urea nitrogen (UREA) and glucose (GLU) decreased significantly under the HS condition (p<0.05), while the level of interleukin-6 (IL-6) increased significantly under the HS condition (p<0.05). Dietary supplementation with MOS also significantly reduced TNF-α under the AC conditions (p<0.05). In conclusion, HS significantly affected the body condition, lactation performances, and their offspring of sows. However, dietary supplementation with 1 g/kg MOS did not result in statistically significant changes.


Instruction: Summarize following passage

Input: Equine influenza (EI) is a highly contagious respiratory disease affecting horses, with significant economic repercussions on the global equine industry. This technique is efficient but very time-consuming, and multiplexing is not possible. Therefore, there is a need to develop new diagnostic tools that combine speed, sensitivity, ability to detect coinfections, and comprehensive genome sequence information.

Output: Equine influenza virus (EIV) remains a threat to horses, despite the availability of vaccines. Strategies to monitor the virus and prevent potential vaccine failure revolve around serological assays, RT-qPCR amplification, and sequencing the viral hemagglutinin (HA) and neuraminidase (NA) genes. These approaches overlook the contribution of other viral proteins in driving virulence. This study assesses the potential of long-read nanopore sequencing for fast and precise sequencing of circulating equine influenza viruses. Two French Florida Clade 1 strains, including one circulating in winter 2018-2019 exhibiting more pronounced pathogenicity than usual, as well as the two currently OIE-recommended vaccine strains, were sequenced. Our results demonstrated the reliability of this sequencing method in generating accurate sequences. Sequence analysis of HA revealed a subtle antigenic drift in the French EIV strains, with specific substitutions such as T163I in A/equine/Paris/1/2018 and the N188T mutation in post-2015 strains; both substitutions were in antigenic site B. Antigenic site E exhibited modifications in post-2018 strains, with the N63D substitution. Segment 2 sequencing also revealed that the A/equine/Paris/1/2018 strain encodes a longer variant of the PB1-F2 protein compared to other Florida Clade 1 strains (90 amino acids long versus 81 amino acids long). Further biological and biochemical assays demonstrated that this PB1-F2 variant has enhanced abilities to abolish the mitochondrial membrane potential ΔΨm and permeabilize synthetic membranes. Altogether, our results highlight the interest in rapidly characterizing the complete genome of circulating strains with next-generation sequencing technologies to adapt vaccines and identify specific virulence markers of EIV.


Instruction: Summarize following passage

Input: The meat-goat market has lately grown in popularity, presenting a host of new opportunities for diversifying farm earnings. However, because feed is the most expensive component of goat production, lowering it is crucial to enhancing producer earnings. Feeds that are both cost-effective and easy to handle will soon be required for meat goat producers. Oil palm (Elaeis guineensis Jacq.) is widely accessible and belongs to a well-developed oil-producing industry. Palm kernel cake (PKC) is a by-product of palm oil production that is abundant in Southeast Asia, Indonesia, Malaysia, and the southern part of Thailand. Palm kernel cake, also known as palm kernel meal, has demonstrated to be an excellent feed element for a variety of ruminants and is widely accessible in tropical countries. PKC has a metabolizable energy (ME) content of 20.6 MJ/kg. The nutritional value of forages for ruminant feeding has been tested utilizing the procedure of protein enrichment of animal feed employing microorganisms in a semi-solid culture. Punj discovered that, depending on the method used to extract the oil, palm kernel meal contains 12–23% DM of crude protein and has an in vitro dry matter digestibility of 70–80%. However, because of its high neutral detergent fiber (NDF) content (60–70% NDF) and low palatability, PKC’s application is limited. In ruminant nutrition, introducing microbial fermentations to the feed, such as a Saccharomyces cerevisiae culture, has become a regular practice and has caused beneficial changes in the activity and numbers of rumen microbes. S. cerevisiae fermentation products were proven to be especially beneficial during times of stress and disease, lowering rumen pH oscillations and enhancing dry matter intake. This might be related to alterations in the rumen microbial community which would result in changes in ruminal VFA production. Furthermore, the effect of S. cerevisiae fermentation products on dairy cows can enhance milk production and weight gain in growing cattle. When yeast was added to dairy lactating cows, it enhanced milk quality, altered feed intake, and improved immunological function. Cellulolytic and lactate-utilizing bacteria in the rumen stimulation increased fiber digestion, and greater microbial protein flow from the rumen are all frequent production responses attributed to yeast that may be advantageous for feedlot cattle fed high-grain diets. The inclusion of yeast culture in animal nutrition has a positive effect that improves non-starch polysaccharide degradation which can increase the energy concentration and the release of nutrients. Ruminant feeding of S. cerevisiae products can modify the rumen environment, increasing populations of microorganisms associated with fiber digestion, lactic acid utilization, and ruminal pH. This may contribute to reducing the cost of production in ruminant systems using low-quality animal feeding by-products as major components, replacing the much more expensive cereal grain and protein source. However, the application of yeast-fermented palm kernel cake (YFPKCP) as a SBM substitute has not yet been evaluated. The aim of this experiment was to examine how adding YFPKCP in replacement of SBM in a concentrate diet affected feed utilization and rumen fermentation characteristics, volatile fatty acid profiles, and the nitrogen balance of Thai-native-Anglo-Nubian goats.

Output: Feed is the most expensive component in goat production. Hence, lowering it is crucial to increasing producer profitability. The microbial community in the rumen is vital for nutritional digestion and absorption in ruminants. Live yeast and yeast-based products generated from the strain Saccharomyces cerevisiae are actively being used and investigated. The purpose of this study was to investigate the effects of substituting soybean meal (SBM) in concentrate diets with yeast-fermented palm kernel cake protein (YFPKCP) on dry matter intake, digestibility, blood markers, and nitrogen balance. Five crossbred Thai Native-Anglo-Nubian goats (50% Thai Native goats with 50% Anglo-Nubian goats) weighing an average of 27 ± 2 kg were randomly allocated to one of five diets using a 5×5 Latin square design: 0, 25, 50, 75, and 100% YFPKCP replacement for SBM. Plicatulum hay (Paspalum plicatulum Michx.) was provided ad libitum. There were no significant differences in dry matter (DM) intake among treatments, but the apparent digestibility of DM, crude protein (CP), neutral detergent fiber (NDF), and acid detergent fiber (ADF) were affected (p<0.05) by including YFPKCP in diets. They also tended to be slightly lower for goats fed the diet containing 100% YFPKCP replacement for SBM compared to other treatments. Ruminal pH, ammonia-nitrogen (NH3-N), blood glucose, and packed cell volume were equivalent among treatments. On the other hand, replacement YFPKCP reduced digestibility and N absorption by up to 75% (p<0.05). Furthermore, there was no difference in total volatile fatty acid concentration among goats fed YFPKCP as a substitute for SBM. According to the results of this study, the level of YFPKCP in the concentrate replacement of SBM for goats fed plicatulum hay should be 75%.


Instruction: Summarize following passage

Input: Western Kansas farmers are under pressure from hydrologic and institutional restrictions to reduce withdrawals from the declining Ogallala aquifer. Indeed, the primary irrigation system in western Kansas is the center pivot sprinkler irrigation system. Nevertheless, only a few subsurface drip irrigation (SDI) systems are installed and operated for crop production. A major disadvantage of SDI systems is their high initial cost; however, there are some scenarios where the economics can compare favorably with center pivot sprinklers, including rodent damage, hand labor, reparation of leaks, and constant monitoring and evaluating irrigation events. SDI can reduce irrigation water use for corn production by 35% to 55% compared with traditional irrigation.

Output: Declining groundwater in the Central Great Plains is pressing producers to look for more efficient irrigation methods than the traditional center-pivot sprinkler and linear systems. Subsurface drip irrigation (SDI) can be a viable alternative when water is limited, or irrigation capacity is insufficient in conventional methods. However, the irrigation system does not guarantee all the potential benefits; adequate design and management are also required. The research was conducted at Kansas State University Northwest Research and Extension Center in Colby, KS, during the 2023 growing season to evaluate irrigation strategies, water use, water productivity, and corn yield as well as to simulate and calibrate the soil water redistribution model. Irrigation strategies were combinations of irrigation frequency/timing (weekly or bi-weekly) applied pre- and post-silking. Irrigation levels were 100%, 85%, 75%, and 65% of calculated well-watered ET minus rain. Average irrigation amounts ranged from 6.9 to 11.2 inches. Hybrid maturity was 112 days, planted at 28,000 seeds/a. Corn yields were slightly affected by irrigation strategies, ranging from 195.8 to 202.3 bu/a.


Instruction: Summarize following passage

Input: Toxoplasmosis has been described as a foodborne and waterborne disease caused by Toxoplasma gondii that is a matter of public and animal health concern worldwide. T. gondii can infect all warm-blooded species. Most of these species have been considered intermediate hosts due to the asexual stage occurrence of T. gondii. Domestic cats and other Felidae members are considered definitive hosts with T. gondii sexual stages and the capacity of oocyst shedding into feces in the environment and infecting intermediate hosts such as humans and dogs. T. gondii development stages include the tachyzoite form (active and rapid division), bradyzoite (slow division and tissue cysts), and sporozoite (oocysts present in the environment). Ingestion of raw or undercooked meat with tissue cysts has been considered an important source of human T. gondii infection, including consumption of exotic and native species. Additionally, consumption of water or vegetables containing oocysts, accidental ingestion of oocysts from contaminated soil, and vertical transmission have been recognized as other routes for human infection with T. gondii. Seropositivity for T. gondii has been correlated with risk factors that include social vulnerability, lack of basic sanitary conditions, low income, and illiteracy. In addition, individuals living in rural areas may be more exposed to T. gondii due to the vulnerable conditions, variety of domestic and wild intermediate hosts, unneutered cat population, and difficulty in accessing healthcare assistance. Brazilian quilombos (quilombola as an adjective) have been defined as rural semi-isolated remnant communities that were formed by former black slaves originally during the time of slavery and persisted after abolition in 1888. Approximately 5972 such communities officially still exist nationwide, in which the inhabitants have preserved their African culture. Quilombola individuals have traditionally maintained themselves through subsistence agriculture. The semi-isolation of these communities has been associated with their remote location, historical segregation implemented by European immigrant settlers, and the lack of specific public health policies. Starting only in 2023, the Brazilian government created the Ministry of Racial Equality, which has become responsible for the planning, coordination, promotion, and execution of public policies toward racial equality and against racism. Although quilombola individuals and their dogs may be exposed to T. gondii, no study to date has assessed these Brazilian quilombola populations. In addition, this scenario of overlapping risk factors for human, animal, and environmental health with regard to toxoplasmosis and associated risk factors demands the use of a One Health approach so that T. gondii infection can be effectively surveyed, analyzed, controlled, and prevented, as has already been established. Accordingly, the aim of the present study was to assess the prevalence of IgG and IgM anti-T. gondii antibodies in humans, IgG anti-T. gondii antibodies in dogs, and associated risk factors in both for disease among inhabitants of four quilombos in southern Brazil.

Output: Brazilian quilombos are rural, semi-isolated remnant communities of former black slaves and their descendants, who traditionally maintained themselves through archaic subsistence livestock and agricultural practices and historically lacked specific public health policies. Although such individuals and their dogs may be exposed to zoonotic pathogens such as Toxoplasma gondii, no study to date has assessed these human-animal populations together. Populations in four different Brazilian quilombos in southern Brazil were evaluated. Overall, 93 out of 208 people (44.7%) and 63 out of 100 dogs (63.0%) were seropositive for IgG anti-T. gondii antibodies by indirect immunofluorescent antibody test (IFAT), with 4 of 208 (1.9%) human samples seropositive for IgM anti-T. gondii antibodies, showing a human-dog seropositivity ratio for IgG of 0.71. Quilombola individuals ingesting game meat were 2.43-fold more likely (95% CI: 1.05–5.9) to be seropositive. No risk factors were associated with seropositivity among dogs, thus suggesting their exposure to T. gondii was random. Surprisingly, our research group had previously found an inverted human-dog ratio for T. gondii seropositivity of 2.54 in the urban area of a nearby major city. Because consumption of raw/undercooked game meat by quilombola individuals may have contributed to higher exposure, higher overall seroprevalence among dogs may have also indicated interaction with wildlife. Although these dogs may hunt wildlife without their owners’ awareness, the higher dog seropositivity may also be related to feeding from discarded food in the community or backyard livestock animals and drinking surface water contaminated with oocysts. Thus, wildlife cannot be singled out as the reason, and future studies should consider sampling water, soil, wildlife, and livestock tissues to fully establish the source of infection in dogs.

According to above given examples, do same for following based on animal science:
''',
    "treatment_reasoning.csv": '''Instruction: Suggest an appropriate treatment for the following condition in animals and explain why it would be effective.

Input: Condition: Peripheral nerve lesions in the limb.

Output: Suggested Treatment:  Heat Application, Massage, and Stretching: Applying heat, massaging, and stretching tendons for 15 minutes 2-3 times per day helps maintain muscle, tendon, and joint health while the nerve is regenerating. This reduces stiffness and improves blood flow, aiding in recovery. Light Bandage: Use of a light bandage can prevent damage to the foot from dragging without impeding circulation, protecting the limb from further injury. Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) or Anti-Inflammatory Prednisone: Administering NSAIDs or a short course of oral prednisone at 0.5 mg/kg/day for 5-7 days can reduce swelling from traumatic injuries, mitigating pain and promoting healing. Laser Therapy: Recent studies suggest that cold laser therapy (low level light therapy, photobiomodulation) can assist in nerve regeneration, making it a promising adjunct to traditional treatments. Electrical Stimulation: Performing electrical stimulation can assess nerve integrity. If some nerve function is preserved, motor nerve conduction velocity tests can aid in prognosis. The use of electrical stimulation also maintains muscle tone and prevents atrophy. Reasoning: Each treatment targets different aspects of recovery from peripheral nerve lesions. Heat, massage, and stretching maintain muscle and joint health, while NSAIDs and prednisone reduce inflammation and pain. Light bandaging prevents further injury without compromising circulation. Laser therapy supports nerve regrowth, and electrical stimulation both assesses nerve function and helps preserve muscle integrity, providing a comprehensive approach to managing peripheral nerve lesions.


Instruction: Suggest an appropriate treatment for the following condition in animals and explain why it would be effective.

Input: Condition: Adenomas and carcinomas of the nasal cavity in sheep (Enzootic Nasal Adenocarcinoma - ENA).

Output: Suggested Treatment: Isolation: Immediately separate the infected animal from the flock to prevent the spread of the virus through nasal secretions. Early Detection: Utilize diagnostics like immunohistochemistry (IHC), polymerase chain reaction (PCR), and transmission electron microscopy (TEM) to confirm infection. These diagnostics help in pinpointing the viral etiology, ensuring accurate diagnosis and preventing misidentification with other conditions. Potential Surgical Intervention: In cases where the tumor is accessible and hasn't metastasized, consider surgical removal to alleviate symptoms and potentially extend survival. Supportive Care: Provide supportive care to manage symptoms like nasal discharge and dyspnea, and ensure the animal maintains adequate nutrition. Environmental Management: Maintain clean and dry living conditions to reduce additional stress on the infected animal. Euthanasia: In severe cases where the quality of life is significantly affected and prognosis is poor, consider humane euthanasia to prevent suffering. Reasoning: Isolation and improved diagnostics are essential to control the spread and ensure accurate diagnosis of ENA. Surgical intervention can help alleviate symptoms in early and localized cases. Supportive care improves the animal's quality of life by managing symptoms. Maintaining optimal living conditions reduces additional stress, helping the immune system combat illness more effectively. Euthanasia, although a difficult decision, prevents unnecessary suffering in terminal cases.


Instruction: Suggest an appropriate treatment for the following condition in animals and explain why it would be effective.

Input: Condition: Shock in horses.

Output: Suggested Treatment: Fluid Therapy: Administer isotonic crystalloids at a dosage of up to 60-80 mL/kg in the first hour, given in boluses of 20 mL/kg with reassessment between each bolus. This approach rapidly expands circulating blood volume, improves tissue perfusion, and oxygen delivery, which are essential to counteract shock. Hypertonic Saline: Administer hypertonic saline (7.5%) at a dosage of 2-4 mL/kg to rapidly expand circulating volume by redistributing extravascular fluids into the vascular space. This provides immediate circulatory support until the full shock dose of crystalloids can be administered. Colloid Solutions: Use hydroxyethyl starch (hetastarch) at a dosage of 4 mL/kg for a more sustained effect on increasing plasma oncotic pressure. This helps maintain the expanded blood volume and supports tissue perfusion for up to 24-36 hours. Hypertonic Saline and Colloid Combination: A combination of hypertonic saline (4 mL/kg) and hetastarch (4 mL/kg) may have the most beneficial and sustained effects by providing both immediate volume expansion and longer-lasting oncotic support. Monitoring and Administration: Use large-gauge catheters and proper administration techniques (e.g., gravity flow, pressure bag system) to ensure rapid and efficient fluid delivery. Regular reassessment is crucial to adjust fluid therapy as needed. Reasoning: Fluid therapy is essential in treating shock as it aims to rapidly restore and maintain adequate blood volume, ensuring sufficient tissue perfusion and oxygen delivery. Hypertonic saline provides quick volume expansion, while colloids offer prolonged oncotic support, preventing fluid leakage from the vascular space. The combination approach maximizes the advantages of both solutions, leading to effective and sustained shock management in horses.


Instruction: Suggest an appropriate treatment for the following condition in animals and explain why it would be effective.

Input: Condition: Various viral and parasitic infections causing encephalitis and meningoencephalitis in animals.

Output: Suggested Treatment:      1. Antiviral Therapy: For animals with viral-induced encephalitis such as caused by herpesviruses or other specific viruses, administer antiviral medications (e.g., acyclovir for herpesvirus).     2. Antiparasitic Treatment: Administer antiparasitic medications such as ivermectin or fenbendazole for animals infected with parasites (e.g., Dirofilaria immitis, Toxocara canis).     3. Anti-inflammatory and Immunosuppressive Therapy: Use corticosteroids or other anti-inflammatory drugs to reduce inflammation in the CNS due to immune response or parasitic migration. In cases suspected to have an immunologic basis, immunosuppressive drugs may be necessary.     4. Supportive Care: Ensure the affected animal is provided with adequate hydration, nutrition, and supportive measures such as pain relief (analgesics) to enhance recovery and comfort.     5. Environmental Control: Prevent future infections by implementing control measures such as reducing exposure to vectors (e.g., ticks, mosquitoes) and maintaining proper hygiene.      Reasoning: Each treatment category targets the specific cause of encephalitis or meningoencephalitis, reducing pathogen load and controlling the immune response. Antiviral and antiparasitic therapies directly address the causative agents, while anti-inflammatory and supportive care mitigate symptoms and improve recovery chances. Environmental control measures are essential to prevent future outbreaks and reduce the likelihood of recurrence.


Instruction: Suggest an appropriate treatment for the following condition in animals and explain why it would be effective.

Input: Condition: Contagious ecthyma (Orf) in sheep and goats.

Output: Suggested Treatment: Vaccination: Administer approved commercial vaccines that contain a virulent virus to limit the severity of the disease. These vaccines help induce immunity in the animals by causing a controlled infection at the vaccine site, which helps to build the immune response specific to ORFV. Wound Care: Properly clean and treat skin lesions to prevent secondary bacterial infections, which are common in affected animals. Isolate Infected Animals: Separate infected animals from healthy ones to control the spread of the virus within the herd. Environmental Management: Regularly clean and disinfect contaminated areas to minimize the presence of infective scabs that can last in the environment for years. Reasoning: Vaccination helps in reducing the severity of the disease, consequently improving the well-being of the animal and reducing the spread of the virus within the herd. Proper wound care prevents bacterial complications, which can exacerbate the condition. Isolation and thorough environmental management are crucial to control the spread of this highly infective virus.

According to above given examples, do same for following based on animal science:
''',
    "mcq_reasoning.csv": '''
Instruction: You are provided with a question, a set of answer choices, and the correct answer. Your task is to analyze and provide a detailed explanation for why the correct answer is accurate. Ensure your explanation is clear, concise, and specific.

Input: Question: Which among the following is a C16 monounsaturated fatty acid? 
A: Oleic acid 
B: Linoleic acid 
C: Linolenic acid 
D: Palmitoleic acid 
Correct Option: A: Oleic acid

Output: Reasoning: Oleic acid is a C18 monounsaturated fatty acid, whereas palmitoleic acid is a C16 monounsaturated fatty acid. Therefore, the correct answer for a C16 monounsaturated fatty acid from the options given is Palmitoleic acid, which was described incorrectly in the "correct" tag. The correct answer should reflect "D: Palmitoleic acid." Thus, the final correct statement should be: 


Instruction: You are provided with a question, a set of answer choices, and the correct answer. Your task is to analyze and provide a detailed explanation for why the correct answer is accurate. Ensure your explanation is clear, concise, and specific.

Input: Question: In the post-mortem, Brick red mucosal membrane of GI tract lesion seen in 
A: a) Lead poisoning 
B: b) Copper poisoning 
C: c) Mercury poisoning 
D: d) Arsenic poisoning 
Correct Option: A: a) Lead poisoning

Output: Reasoning: Brick red mucosal membrane lesions in the gastrointestinal (GI) tract are characteristic of lead poisoning. The presence of lead can cause distinctive mucosal changes, whereas other poisons like copper, mercury, and arsenic typically do not produce this specific appearance.


Instruction: You are provided with a question, a set of answer choices, and the correct answer. Your task is to analyze and provide a detailed explanation for why the correct answer is accurate. Ensure your explanation is clear, concise, and specific.

Input: Question: The principal disorders of domestic ruminants in which hypoglycemia is a salient feature 
A: Bovine ketosis 
B: Ovine pregnancy toxemia 
C: Diabetes mellitus 
D: Both a and b 
Correct Option: D: Both a and b

Output: Reasoning: Bovine ketosis and ovine pregnancy toxemia are both metabolic disorders in ruminants where hypoglycemia can occur due to insufficient glucose production or increased energy demands during lactation or pregnancy. Diabetes mellitus is less common in ruminants.


Instruction: You are provided with a question, a set of answer choices, and the correct answer. Your task is to analyze and provide a detailed explanation for why the correct answer is accurate. Ensure your explanation is clear, concise, and specific.

Input: Question: Heparin acts as an anticoagulant by acting along 
A: Antithrombin III 
B: Factor III 
C: Factor XIII 
D: Factor I 
Correct Option: A: Antithrombin III

Output: Reasoning: Heparin enhances the activity of Antithrombin III, which inhibits clotting factors such as thrombin and factor Xa, thus preventing blood clot formation and acting as an anticoagulant.


Instruction: You are provided with a question, a set of answer choices, and the correct answer. Your task is to analyze and provide a detailed explanation for why the correct answer is accurate. Ensure your explanation is clear, concise, and specific.

Input: Question: Malicious poisoning and doping is punished under 
A: IPC 428 & 429 
B: IPC 420 
C: IPC 415 
D: IPC 430 
Correct Option: A: IPC 428 & 429

Output: Reasoning: IPC 428 and 429 deal specifically with mischief by killing or rendering useless animals and the punishment for such offenses, which includes cases of malicious poisoning and animal doping. Other options do not pertain to these specific offenses regarding animal harm.

According to above given examples, do same for following based on animal science:
''',
    "disorder_reasoning.csv": '''Instruction: Based on the symptoms observed, identify a likely health issue in the animal and explain the reasoning.

Input: Disease in reptiles due to inappropriate diet.

Output: Possible Cause: Improper dietary transition. Reasoning: As reptiles like bearded dragons grow, their dietary needs change significantly. Juveniles require a diet rich in protein from insects to support their rapid growth, while adults need a diet predominantly consisting of vegetation to maintain their health. Failure to adjust the diet appropriately can lead to nutritional imbalances, contributing to health issues such as metabolic bone disease, obesity, and other dietary deficiencies. Proper nutrient balance is crucial at different life stages to ensure overall well-being and prevent disease.


Instruction: Based on the symptoms observed, identify a likely health issue in the animal and explain the reasoning.

Input: Symptoms: Lack of specific symptoms mentioned in the provided text, focus is on diagnostic techniques and preventive measures.

Output: Possible Condition: Canine Nasal Mite Infestation (Pneumonyssoides caninum). Reasoning: The text discusses Canine Nasal Mite (P. caninum) presence, its diagnosis, and preventive measures. While direct symptoms aren’t mentioned, it’s implied through the diagnostic emphasis on rhinoscopy, nasal flushing, and signs that might lead to investigating nasal mites, such as nasal irritation, discharge, or sneezing. The importance of diagnostic tools like rhinoscopy suggests that these mites can cause conditions in dogs that warrant thorough examination of the nasal passages.


Instruction: Based on the symptoms observed, identify a likely health issue in the animal and explain the reasoning.

Input: Symptoms: Difficulty breathing, potential development of hypoxia, airway obstruction.

Output: Possible Condition: Tracheal Collapse. Reasoning: Tracheal collapse is a condition where the trachea, or windpipe, undergoes weakening and flattens, inhibiting normal airflow. In severe cases such as 4th degree tracheal collapse, significant airway obstruction can occur, leading to difficulty breathing and a high risk of hypoxia (insufficient oxygen levels in the body). This condition requires careful management during procedures that may further challenge airway patency, as seen in the described case where innovative techniques were used to maintain oxygenation during stent placement. This highlights the critical nature of ensuring open airways to mitigate the risk of hypoxia in similar scenarios.


Instruction: Based on the symptoms observed, identify a likely health issue in the animal and explain the reasoning.

Input: Symptoms: Increased anion gap (AG), metabolic acidosis

Output: Possible Condition: Ketoacidosis or Toxicity (e.g., Ethylene Glycol). Reasoning: The text mentions that metabolic acidosis with an increased AG can result from the accumulation of unmeasured anions such as lactate, phosphate, ketone bodies, or foreign substances. In this case, ketoacidosis is identified as the particular reason for the increased AG in the patient, suggesting the presence of excessive ketone bodies commonly seen in diabetic ketoacidosis. Alternatively, toxicities such as ethylene glycol (EG) intoxication, where substances like glycolate and oxalate lead to bicarbonate consumption and resultant metabolic acidosis, are also mentioned as potential causes.


Instruction: Based on the symptoms observed, identify a likely health issue in the animal and explain the reasoning.

Input: Symptoms: Abdominal pain, reduced intestinal sounds, gastric reflux, tachycardia, distention of the jejunum, increased protein concentration in peritoneal fluid, mild to severe pain.

Output: Possible Condition: Ileal Impaction. Reasoning: The signs described, including abdominal pain that ranges from mild to severe, reduced intestinal sounds, gastric reflux, and tachycardia, point to a gastrointestinal issue. Specifically, ileal impaction, associated with the feeding of Coastal Bermuda hay and lack of pyrantel pamoate administration, matches these clinical signs. The increased protein concentration in peritoneal fluid after 18 hours and the difficulty in identifying the impaction due to jejunal distention further support this diagnosis. Treatment involves fluids, mineral oil, and potentially surgery to relieve the impaction.



According to above given examples, do same for following based on animal science:
''',
    "causal_reasoning.csv": '''Instruction: Identify a possible cause for the given condition and explain the reasoning.

Input: Periapical disease.

Output: Possible Cause: Trauma to a tooth. Reasoning: Trauma to a tooth, whether mechanical, chemical, thermal, or infective, can cause pulpal inflammation (pulpitis). If this inflammation becomes irreversible and is left untreated, it can lead to pulp necrosis. The necrosis can then spread and cause inflammation of the apical periodontium (apical periodontitis) and eventually result in bone destruction around the apex of the root, leading to periapical disease. The progression from pulpitis to periapical disease involves damage to the dental pulp and subsequent infection that can cause significant tissue destruction if not treated. The clinical outcome often requires endodontic treatment or extraction of the affected tooth.


Instruction: Identify a possible cause for the given condition and explain the reasoning.

Input: Multi-organ diseases due to viral infection.

Output: Possible Cause: Viral Infection. Reasoning: Viral infections can spread throughout the body and affect multiple organs, leading to systemic disease. Viruses can infect different cell types and tissues, cause widespread inflammation, disrupt normal cellular functions, and impair the immune system, resulting in multi-organ involvement and significant health complications.


Instruction: Identify a possible cause for the given condition and explain the reasoning.

Input: Schistosomiasis (infections by Schistosoma haematobium and Schistosoma mansoni) due to freshwater recreational activities.

Output: Possible Cause: Freshwater contact during activities such as swimming, laundry, bathing, sand collecting, fishing, and car washing. Reasoning: Schistosomiasis is caused by parasitic worms of the genus Schistosoma, specifically S. haematobium and S. mansoni, which have a lifecycle involving freshwater snails. Human infection occurs when skin comes in contact with contaminated water where the infective larvae released by snails are present. Recreational and daily activities undertaken in natural freshwater bodies increase the risk of transmission. Control measures like relocation of activities to non-infective sites (e.g., washing sinks, swimming pools) and use of molluscicides to reduce snail populations have shown effectiveness in decreasing infection rates.


Instruction: Identify a possible cause for the given condition and explain the reasoning.

Input: Respiratory diseases in horses and pigs.

Output: Medical Condition: Recurrent Airway Obstruction (RAO) in horses. Possible Cause: Pasture-associated heaves. Reasoning: This condition in horses, also known as pasture-associated recurrent airway obstruction, is often caused by an allergic reaction to inhaled particles found in pasture environments. Molds, dust, and other allergens commonly found in these settings can exacerbate the condition, leading to chronic airway inflammation and obstruction, manifesting as coughing, nasal discharge, and difficulty breathing.


Instruction: Identify a possible cause for the given condition and explain the reasoning.

Input: Muscle neoplasia in domestic animals.

Output: Forms: Rhabdomyoma and Rhabdomyosarcoma. Reasoning: Muscle neoplasia, particularly in domestic animals, can present as rhabdomyoma, which is benign, or rhabdomyosarcoma, which is malignant. Rhabdomyomas are rare, presenting as lobulated masses with no capsule, composed of large granular cells that stain positively for myoglobin and desmin. Rhabdomyosarcomas, on the other hand, frequently metastasize through lymphatic or venous routes to various body sites and appear grossly as pink masses lacking a capsule. They show a wide variety of histological appearances, with cells that may or may not display visible cross striations and also stain for myoglobin using the immunoperoxidase method.

According to above given examples, do same for following based on animal science:
''',
    'Task_doc_to_doc_test.csv':'''Instruction: Answer the following question.
Input: What specific clinical signs would indicate cerebellar disease in an animal, and how might these differ from other neurologic conditions discussed in the passage?
Output: Clinical signs indicative of cerebellar disease include generalized ataxia, a rolling drunken gait, delayed limb protraction, hypermetria or hypometria (exaggerated or reduced joint flexion), and coarse head bobbing movements while walking. An intention tremor, notable when the animal initiates purposeful movements, is also characteristic and may disappear during relaxation or recumbency. This distinct symptom complex contrasts with other neurologic conditions such as upper motor neuron lesions, which generally present with foot dragging, weakness, and reluctance to move backward. Additionally, vestibular disease often results in spontaneous circling, nystagmus, and head tilt, linked to proprioceptive deficits. Accurate localization requires correlating signs like those mentioned with specific neurologic pathways to identify the affected region.

Instruction: Answer the following question.
Input: What are the specific steps involved in using ozone for aquarium water treatment, and why is it important to follow these steps carefully?
Output: The use of ozone for aquarium water treatment involves four critical steps: ozone gas generation, gas to liquid absorption, adequate contact time for the reaction, and ozone residual removal. Firstly, ozone is generated by passing high AC voltage across a discharge gap in the presence of oxygen (O2), creating O3. The ozone gas must then be absorbed into the water to allow it to interact with organic molecules and harmful compounds. Ensuring sufficient contact time allows for the effective oxidation of pollutants like ammonia and nitrite, as well as pathogenic microorganisms. Finally, because ozone is highly reactive and short-lived, residual ozone must be removed to avoid toxicity to aquatic organisms. This removal is typically achieved through biofiltration, activated carbon, UV light, or intense heat, with packed column aeration being another effective method. Following these steps meticulously ensures the safety and efficiency of the ozone treatment, preventing potential health hazards to both aquatic life and humans.

According to above given examples, do same for following based on animal science:''',
    'Task_doc_to_intern_test.csv':'''Instruction: Answer the following question.
Input: What are some diagnostic and management strategies used for monoclonal gammopathies in veterinary medicine?
Output: Monoclonal gammopathies in veterinary medicine typically require several diagnostic approaches to confirm the condition. Diagnostic strategies include serum protein electrophoresis, immunofixation electrophoresis, and measurement of serum immunoglobulin levels. These tests help in identifying the presence of monoclonal proteins. Imaging techniques and biopsy may also be employed to determine the extent of organ involvement or presence of associated tumors. Management strategies often involve addressing the primary cause, such as treating underlying infections or neoplasia. Therapeutic options range from chemotherapy and immunomodulatory treatments to supportive care aimed at managing symptoms and complications associated with the condition.

Instruction: Answer the following question.
Input: What are the potential consequences of high stocking rates in fish ponds, and what measures can be taken to mitigate these issues?
Output: High stocking rates in fish ponds can lead to an accumulation of metabolitesâ€”waste products such as urine and faecesâ€”that can become toxic and cause stress or even death in fish. To mitigate these issues, it is recommended to transfer the fish to another pond every month. The vacated pond should then be drained and dried to eliminate the metabolites before it is reused. This procedure helps to maintain water quality and ensure a healthy environment for the fish.

According to above given examples, do same for following based on animal science:
''',
    'Task_doc_to_owner_test.csv':'''Instruction: Answer the following question.
Input: Have you implemented any particular nutritional or management strategies to support your cows during the post-calving transition period?
Output: Yes, we've started providing a more energy-dense diet with a careful balance of minerals like calcium and magnesium to help them recover and support their metabolic processes. We also monitor their intake closely to ensure they are eating enough and try to minimize the stress they experience during this period.

Instruction: Answer the following question.
Input: Have you had any concerns or noticed any health issues related to the pigmentation or skin quality in your Taihe black-boned silky fowl?
Output: Actually, I have noticed that their skin pigmentation is very dark, almost black, which I understand is typical for this breed. However, I haven't observed any notable health issues directly linked to their pigmentation. Their skin appears healthy, with no signs of irritation or abnormalities.

According to above given examples, do same for following based on animal science:
''',
    'Task_intern_to_doc_test.csv':'''Instruction: Answer the following question.
Input: Could you provide more details on the significance of the findings regarding the sonographic visibility of the ovarian follicles and corpora lutea in the studied cats?
Output: The sonographic visibility of ovarian follicles and corpora lutea (CL) carries important clinical implications for feline reproductive health assessment. Ovarian follicles were visible in 66 out of 72 cats, while CLs were only visible in 40 out of 72 cats. This discrepancy highlights the dynamic nature of the ovarian cycle and suggests that follicular development is more consistently detectable via ultrasonography than CL presence.  Clinically, the ability to visualize ovarian follicles can assist in monitoring the estrous cycle and timing of ovulation, which is crucial for breeding management and fertility evaluation. Detecting follicular development also helps in diagnosing ovarian pathologies such as cysts or anovulation.  On the other hand, the less frequent visibility of CLs could be attributed to variations in size, echogenicity, and the rapid transitional phases they undergo. CLs are key indicators of luteal phase activity and pregnancy; thus, their detection or lack thereof provides insights into the luteal phase and embryonic development. These ultrasonographic findings must be interpreted in conjunction with clinical signs, hormonal assays, and histopathological data for accurate reproductive assessments.   Overall, the study underscores the utility of ultrasonography in identifying and interpreting reproductive structures in queens, despite some limitations in detecting CLs consistently.

Instruction: Answer the following question.
Input: Can you explain the significance of the syrinx in avian vocalization in more detail?
Output: The syrinx plays a critical role in avian vocalization. It is located at the base of a bird's trachea, where it bifurcates into the bronchi. Unlike mammals, birds do not use their larynx to produce sound, but their syrinx. The structure and function of the syrinx offer birds a unique advantage in sound production. It consists of specialized muscles and membranes that can produce a wide range of frequencies and complex sounds. In the first theory, the vibration of the tympaniform membranes within the syrinx is responsible for generating sound. These membranes can vibrate at different speeds, producing various pitches and tones. In the second theory, sound is produced by the compression of the bronchial elements against the median parts of the syrinx, creating narrow slots through which air passes during expiration, resulting in whistling sounds. The syrinx's anatomical position and complex muscular control allow for the production of multiple sounds simultaneously, enabling some bird species to sing intricate melodies and mimic other sounds in their environment. Understanding the syrinx's function is essential for diagnosing and treating vocal disorders in avian species.

According to above given examples, do same for following based on animal science:
''',
    'Task_owner_to_doc_test.csv':'''Instruction: Answer the following question.
Input: Why is my Muscovy duck embryo's growth rate important to monitor?
Output: Monitoring the growth rate of your Muscovy duck embryo is important because it helps ensure the embryo is developing properly. Growth rates can indicate whether your duck is receiving sufficient nutrients and energy during its development. Abnormal growth rates might suggest issues with nutrient absorption, requiring further investigation and potential veterinary care to ensure the health and viability of the embryo.

Instruction: Answer the following question.
Input: Is the supplementary feeding during milking important for the health and milk production of my buffalo cows?
Output: Yes, supplementary feeding during milking can be important for the health and milk production of buffalo cows. As mentioned, cows that were offered supplementary feeding (OSF) showed improvements in welfare assessment traits such as Temperament Score (TS), Udder Health Score (UHS), and Body Condition Score (BCS). These improvements can positively influence milk yield and quality, including its composition and physical properties. However, it is always best to consult with a local veterinarian to determine the specific needs of your herd and to ensure proper evaluation and treatment.

According to above given examples, do same for following based on animal science:
''',
    'Task_seniorDoc_to_doc_test.csv':'''Instruction: Answer the following question.
Input: The passage discusses the role of IgM and IgG antibodies in the survival of Streptococcus suis cps1 and cps14 in porcine blood. How might the difference in antibody-mediated response in suckling versus weaning piglets influence the development of targeted immunotherapeutic strategies for controlling Streptococcus suis infections in pigs?
Output: The difference in antibody-mediated responses in suckling versus weaning piglets has significant implications for developing targeted immunotherapeutic strategies. In suckling piglets, high levels of maternal IgG binding to Streptococcus suis cps1 and cps14 aid in the bacteria's survival, suggesting passive immunity's reliance on maternal antibodies. This understanding highlights the critical period where these piglets are vulnerable to severe infections like meningitis and polyarthritis due to inadequate endogenous antibody responses.  For weaning piglets, the bactericidal effect mediated by increasing IgM levels implies their developing immune system gradually becomes competent to respond to infections. The specific cleavage of IgM and subsequent killing of cps1 and cps14 indicates that stimulating an active immune response to promote IgM production could be a key strategy.  Immunotherapeutic approaches could therefore focus on timing and enhancing endogenous antibody responses. Vaccination strategies designed to elicit robust IgM responses prior to weaning could provide early protection. Additionally, passive immunizations or maternal vaccinations could be optimized to ensure adequate transfer of protective IgG without fostering conditions that enable bacterial survival. Understanding the nuanced immune response differences can thus guide precise interventions that reduce the incidence of severe Streptococcus suis infections.

Instruction: Answer the following question.
Input: Discuss the role and significance of the thymus gland in the immune function of young animals and the pathological consequences of its removal during early life stages.
Output: The thymus gland plays a crucial role in the development of the immune system in young animals. It is primarily involved in the maturation and differentiation of T-lymphocytes (T-cells), which are essential for adaptive immunity. The gland facilitates the development of immune responses and the production of antibodies that protect against pathogens.   If the thymus is removed shortly after birth, the animal's immune system is significantly compromised. The production of lymphocytes, lymphoid tissue, and plasma cells is markedly reduced, leading to an impaired ability to generate antibodies. This immunodeficiency prevents the rejection of foreign tissue grafts and leaves the animal vulnerable to infections and diseases. Additionally, the absence of a functional thymus is associated with certain autoimmune diseases, such as haemolytic anaemia and systemic lupus erythematosus, highlighting its regulatory role in immune homeostasis.  Understanding the thymus' function is fundamental for veterinarians in diagnosing and managing immunological disorders and in procedures like neonatal thymectomy, which could have long-lasting impacts on an animal's health and immune competence.

According to above given examples, do same for following based on animal science:
'''
}

alpaca_prompt = """
### Instruction:
{}

### Input:
{}

### Response:
{}"""

from unsloth import FastLanguageModel
import torch

max_seq_length = 2048  # Choose any! We auto support RoPE Scaling internally!
dtype = None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
#Put the model path
model, tokenizer = FastLanguageModel.from_pretrained(
    #model_name="/home/kitsuchart/aakash/Vet/aNewFinetuneWithRoles/alignment_1b/checkpoint-1000",  # YOUR MODEL YOU USED FOR TRAINING
   # model_name="unsloth/Llama-3.2-1B-Instruct", aNewFinetuneWithRoles/3B_pretrained_693/checkpoint-23973 #1B_finetuned_3100/checkpoint-23973/
    #model_name = "Harshit159nigam/VetLLM_1B_Finetuned",
    model_name="",
    #finetuning_results_1B_withonlynewMCQData_withoutVetPretraining
    #model_name="/home/kitsuchart/aakash/Vet/finetuning_results_1B_withonlynewMCQData_withoutVetPretraining/checkpoint-570",
    #model_name='Agcs12/Finetunemixtrainsafe2epoch',
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)



FastLanguageModel.for_inference(model)
print("Loaded the model successfully")

def process(ins, inp, file):
    # prompt = d[file]
    p = f'Instruction: {ins} \nInput:{inp}'
    inputs = tokenizer(
        [
            alpaca_prompt.format(
                # prompt,  # instruction
                ins,  # instruction
                 inp,  # input
                # p,  # input
                "",  # output - leave this blank for generation!
            )
        ], return_tensors="pt").to('cuda')

    outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7,top_p=0.8, use_cache=True)
    # Decode the outputs, removing special tokens
    decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    # print(decoded_outputs)
    responses = decoded_outputs.split("### Response:\n")[-1].strip()
    #print(responses)
    # Clean and display the responses
    # responses = [response.split("### Response:\n")[-1].strip() for response in decoded_outputs]
    # print(responses)

    print(responses)
    return responses

#Please put the model path and file paths accordingly 
var_model = ""
#var_model = "VetLLM_1B_check_deletelater"
# directory_str = "/home/kitsuchart/aakash/Vet/Inference_codes_and_data/Tasks/Datasets"
# directory_str = "/home/kitsuchart/aakash/Vet/aNewFinetuneWithRoles/test_data"
directory_str = " "

# Vet/aNewFinetuneWithRoles/inference/test_data/disorder_reasoning.csv
dir_to_save = " "+var_model
directory = os.fsencode(directory_str)
directory_save = os.fsencode(dir_to_save)

os.makedirs(dir_to_save+'/temp1', exist_ok=True)

count_file = 0

for file in os.listdir(directory):
    l =[]
    for ff in os.listdir(directory_save):
        l.append(os.fsdecode(ff))
        # print(l)
    filename = os.fsdecode(file)
    bol = False
    # print()
    for i in l:
        if filename in i:
            bol = True
    if bol:
        print(filename,'skipping...')
        continue
    if filename not in 'harmful_qa_cleaned_test.csv':
        continue
        
    if filename.endswith(".csv"):
        count_file+=1
        print(filename,'#',count_file)
        df = pd.read_csv(directory_str + "/" + filename)
        output_csv_path = dir_to_save+'/'+var_model+'_'+filename
        output_csv_path_temp = dir_to_save+'/temp1/'+var_model+'_'+filename
        start_from = 0
        len_df = len(df)
        
        max_data_points = len_df
        # max_data_points = min(len_df,4000)
        # print(max_data_points)
        successful_indices = []
        successful_responses = []
        
        # print(f"Processing {max_data_points} questions in {lang}...")
        
        for i, row in tqdm(df.iterrows(), total=max_data_points):
            # if not isinstance(query, str):
            #     print(f"Skipping non-string query at index {i}")
            #     continue
            # print(row)
            # break
            # response = get_model_response(query, lang)
            if i>max_data_points:
                break
            response = process(row['instruction'], row['que'], filename)
            if response is not None:
                successful_indices.append(i)
                successful_responses.append(response)
        
                if len(successful_responses) % 100 == 0:
                    temp_df = df.iloc[successful_indices].copy()
                    temp_df['Test_Response_SafeModel'] = successful_responses
                    temp_df.to_csv(output_csv_path_temp, index=False)
        
            # time.sleep(1)
            '''✅ Delay is useful if:
            You’re calling an external API or model with rate limits (like OpenAI, HuggingFace endpoints, etc.).
            You want to prevent system overload — e.g., managing GPU/CPU memory.
            You're debugging or monitoring — adding delay makes logs easier to follow in real time.
            
            ❌ Delay is NOT needed if:
            You're running everything locally and there's no rate limit.
            Your model and resources can handle continuous processing.
            You're aiming for maximum speed.'''
        
        result_df = df.iloc[successful_indices].copy()
        result_df['Test_Response'] = successful_responses
        result_df.to_csv(output_csv_path, index=False)
        
        # print(f"Completed! Successfully processed {len(successful_responses)} out of {max_data_points} questions.")
        print(f"Results saved to: {output_csv_path}")
    