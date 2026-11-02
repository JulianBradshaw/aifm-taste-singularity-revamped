## Likelihood of Taste-Only Singularity V2

[*Julian Bradshaw*](https://www.lesswrong.com/users/julian-bradshaw)

*AI disclosure: I worked with Claude Opus 5.5 and Claude Fable 5.1 to brainstorm, research, and generally think through my work. The custom version of the AIFM was made by Fable 5.1 and Opus 5.5 at my direction; the original custom version also involved GPT-6 Astra. The written text here is my own except for copyediting and the inevitable indirect influence of reading AI writing.*

*Epistemic status: The custom version of the AIFM uses adjustments to the handling of λ which I think are reasonable, a variety of trivial bug fixes which I am \~70% confident in, and an adjustment to hold β fixed when increasing the Infinite Coding Labor Asymptote which I think is reasonable given the assumption that the Asymptote is rising over time. I am \~90% confident λ is rising over time and think that it’s best modeled as within the range \[0.6, 0.9\] over the timespan to ASI, \~80% confident the Asymptote is rising but very uncertain of its expected value during takeoff \[10x, 75x\], and 75% confident the distinction between research taste for “direction to research” vs. research taste for “design experiments that hill-climb specified goals” is meaningful, though of course I presume both were taken into account when the AIFP estimated research taste parameters. More important than all that, I think that if I put 40 hours of work into estimating more AIFM parameters, I’d say 80% chance my p(taste-only) would both meaningfully change and have a different confidence interval.*

I think it is \~62% likely there will be a taste-only singularity. Core range: \[0.52, 0.71\]

I used a [custom version of the AI Futures Model](https://github.com/JulianBradshaw/aifm-taste-singularity-revamped) to calculate that probability. My changes were:

1. Adjusted handling of λ so that calibration effects don’t turn higher λ into longer timelines.[^1]  
2. A variety of trivial bug fixes AI identified which don’t shift model behavior much.[^2]  
   1. Of these 14 bug fixes I only rigorously verified 1\.  
3. Hold β fixed when increasing the Infinite Coding Labor Asymptote.

I’m mostly using Eli’s parameters as they reflect my thinking most closely, but with some key differences:

1. Vary λ from 0.60 to 0.90 because λ appears to be rising with newer models.[^3]  
2. Vary the Infinite Coding Labor Asymptote from 10x to 75x because this can rise over time with improved technology.  
3. Vary Research Taste Slope across values of 3.98, 3.34, and 2.70. These are values backcalculated from a new concept: “effective research taste”.

When I started this work, I had expected that my differing values for λ and the Infinite Coding Labor Asymptote would affect p(taste-only). However I realized partway through that, because I’m deliberately blocking their calibration effects on β, they have no effect on p(taste-only).  
After further thought, I still believe it is correct to block the calibration effects on β, because I expect those values to be higher in the future, not that they were wrong as of 2026.5. However, that does make writing about them somewhat beside the point\! I describe my changes to the parameters nevertheless in order to explain my modified AIFM and broader thinking.

#### Higher values of λ

Copying Toby Ord’s [method](https://www.lesswrong.com/posts/6cb7qd3RSkgnviCpf/swarm-scaling#:~:text=careful%20regressions%20and-,got%20values,-\(and%20confidence%20intervals) for backing out estimates of λ from model system cards, I get values of λ \= 0.62, 0.64, 0.66 for Opus 5.5 and λ ≈ 0.66-0.78 for Sonnet 5.5. Toby got λ \= 0.48, 0.57, 0.68 for GPT-5.6. I expect that λ will improve over time as newer models are trained to better coordinate and as harnesses are upgraded. ([further thoughts](https://www.lesswrong.com/posts/EnpJ29asosMKcFGL8/swarm-organization-as-the-exponent-on-test-time-compute))

#### Higher Infinite Coding Labor Asymptote

I feel comfortable varying this parameter a fair amount because the justification in the Supplementary Materials is relatively light: 5x uplift multiplier for a superhuman coder, then another 3x for how much you could possibly improve experiment implementation speed. [Philip Trammell presents](https://philiptrammell.com/static/Parallelizability.pdf) a strong argument for expecting limits on parallelization to rise over time, paraphrased: “technology has raised limits to parallelization consistently in the past; indeed, this is necessary for past exponential technological growth to have lasted”. ([further thoughts](https://www.lesswrong.com/posts/Gi4mzoupy2NqsoL7d/examining-ai-swarm-efficiency-with-the-ai-futures-model#Bonus__How_to_see_shorter_timelines_))

#### Effective Research Taste

I’ve divided taste into two parts: a.) Choosing a problem to work on (*m\_direction*); b.) Designing a good experiment to investigate a given problem (*m\_experiment*).

Based on evidence like [TasteVal](https://arxiv.org/pdf/2610.06824) I think *m\_exp* is growing quickly. Given a particular problem to hill-climb, models can design solid experiments, and this ability is improving rapidly. I do think TasteVal is on the aggressive side: Epoch’s [InnovationEval](https://epoch.ai/publications/innovationeval) and [“Can AI automate Epoch?”](https://epoch.ai/publications/can-ai-automate-epoch) suggest weaker experiment design ability. But the latter are point-in-time estimates only, so I will use just TasteVal for estimating growth of *m\_exp*.

I think *m\_dir* is growing more slowly. This is related to what I call “Relevance Realization” ([full explanation](https://www.lesswrong.com/posts/ybhJbJK3XTXNwyBy5/relevance-realization-as-human-comparative-advantage)); essentially, models are not so good at identifying what’s important to hill-climb on in the first place. This is *related* to designing good experiments too—you want to design an experiment that produces the evidence most likely to substantially update your beliefs—but I think “choose right direction for new AI paradigm” is more an *m\_dir* question, and the more important factor for a taste-only singularity.

I combine *m\_dir* and *m\_exp* via a weighted arithmetic mean, where “w” weights *m\_dir*, and calculate estimates of p(taste-only) at w \= 0.4, 0.6, and 0.8. I keep *m\_dir* at Eli’s implicit value of 0.24. I set *m\_exp* at 0.615 based on TasteVal’s finding that (given a problem) experimental taste doubles every 4.6 points of ECI. β remains, thanks to removed calibration effects, at Eli’s 0.319.

Combined *m* results: w \= 0.4, 0.6, 0.8 ➡ *m* \= 0.465, 0.390, 0.315  
p(taste-only) results: w \= 0.4, 0.6, 0.8 ➡ p(taste-only) \= 71%, 62%, 52%  
(from 300-sample Monte Carlo on Eli’s distribution on custom AIFM; default p(taste-only) here is 40%)

[^1]:  Summary of changes [here](https://www.lesswrong.com/posts/Gi4mzoupy2NqsoL7d/examining-ai-swarm-efficiency-with-the-ai-futures-model#Modifying_the_AI_Futures_Model). My full LW post includes a fun exploration of how the relevant parts of the AIFM work\!

[^2]:  14 bug fixes in total, of which 1 I’ve rigorously verified. Not coincidentally, that 1 fix is the only one I’ve submitted as [a pull request against the AIFM public repo](https://github.com/AI-Futures-Project/aifm-public/pull/1). A repo with just the 14 bug fixes is [here](https://github.com/JulianBradshaw/aifm-vibecoded-fixes).

[^3]:  Although on some tasks I think λ \> 1 [will be measured in the future](https://www.lesswrong.com/posts/EnpJ29asosMKcFGL8/swarm-organization-as-the-exponent-on-test-time-compute#Conclusion), I’ve updated my estimate of “the fraction of tasks that benefit strongly from an agent swarm” lower recently. It’s notable that ex. recent OpenAI math results were *not* swarm-based and that I still have limited use for multi-agent systems.