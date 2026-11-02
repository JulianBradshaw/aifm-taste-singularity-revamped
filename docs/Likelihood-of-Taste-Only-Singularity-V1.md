## Likelihood of Taste-Only Singularity

[*Julian Bradshaw*](https://www.lesswrong.com/users/julian-bradshaw)

*AI disclosure: I worked with Claude Opus 5.5 and Claude Fable 5.1 to brainstorm, research, and generally think through my work. The written text is my own except for copyediting and the inevitable indirect influence of reading AI writing.*  
*Epistemic status: Did not have time to check work. New custom version of AIFM model is based on custom version I’m confident in, but I’m not confident in new changes. I’d like to take more time estimating parameters here and doing full Monte Carlo runs.*

I think it is \~65% likely there will be a taste-only singularity. Core range: \[.55-.71\]

I used a [custom version of the AIFM model](https://github.com/JulianBradshaw/aifm-taste-singularity) to calculate that probability. The custom changes are:

1. Adjusted handling of λ so that calibration effects don’t turn higher λ into longer timelines.[^1]  
   1. This means that increasing λ has no effect on the odds of a taste-only singularity. It does make takeoff faster though, \~10-20% from λ \= .5 to .9.  
2. Holds β fixed when increasing the Infinite Coding Labor Asymptote.  
   1. I think that Asymptote is reasonably modeled at 15x *now* but will rise over time *later*. I don’t want calibration effects to change the original estimate of β.  
   2. Again, this means that increasing the Asymptote has no effect on the odds of a taste-only singularity. It does make takeoff much faster though, \~20-30% when looking at values of Asymptote \= 15x to 50x.

I’m mostly using Eli’s parameters as they reflect my thinking most closely, but with some key differences:

1. Look at λ from 0.65 to 0.90 because λ appears to be rising with newer models[^2]  
2. Look at the Infinite Coding Labor Asymptote from 15x to 50x, because this can rise over time with improved technology  
3. Look at Research Taste Slope values of 3.07, 3.73, and 4.38. These are values backcalculated from a new concept: “effective taste”.

Justifying these differences in turn:

### Higher values of λ

Copying Toby Ord’s [method](https://www.lesswrong.com/posts/6cb7qd3RSkgnviCpf/swarm-scaling#:~:text=careful%20regressions%20and-,got%20values,-\(and%20confidence%20intervals) for backing out estimates of λ from model system cards, I get values of λ \= 0.62, 0.64, and 0.66 from benchmarks on the Opus 5.5 system card's section 8.12, and a more imprecise λ ≈ 0.66-0.78 on the Sonnet 5.5 system card's Fig. 8.12.1.A. Toby got λ \= 0.48, 0.57, 0.68 on different benchmarks for GPT-5.6. I expect that λ will improve over time, considering newer models are deliberately trained to better coordinate, and coordination frameworks are being developed.

### Higher Infinite Coding Labor Asymptote

I feel comfortable varying this parameter a fair amount. The justification in the Supplementary Materials is relatively light: 5x uplift multiplier for a superhuman coder, then another 3x for how much you could possibly improve experiment implementation speed. Also, [Philip Trammell presents](https://philiptrammell.com/static/Parallelizability.pdf) a strong argument for expecting this Asymptote to rise over time. No space to recapitulate here. See also my writing [here](https://www.lesswrong.com/posts/Gi4mzoupy2NqsoL7d/examining-ai-swarm-efficiency-with-the-ai-futures-model#Bonus__How_to_see_shorter_timelines_).

### Effective Taste

I’ve divided taste into two parts: 

1. Choosing a problem to work on (m\_direction)  
2. Designing a good experiment to investigate a given problem (m\_experiment)

Based on evidence like [TasteVal](https://arxiv.org/pdf/2610.06824) I think m\_experiment is growing quickly. Given a particular problem to hill-climb, models can design solid experiments, and this ability is improving rapidly. I do think TasteVal is on the optimistic side: Epoch’s [InnovationEval](https://epoch.ai/publications/innovationeval) and [“Can AI automate Epoch?”](https://epoch.ai/publications/can-ai-automate-epoch), while only providing point-in-time data, suggest weaker experiment design ability.

However I think m\_direction is not growing so quickly. This is related to a problem called “Relevance Realization” ([my summary of that](https://www.lesswrong.com/posts/ybhJbJK3XTXNwyBy5/relevance-realization-as-human-comparative-advantage)); essentially, models are not so good at identifying what’s important to hill-climb on in the first place. This is *related* to designing good experiments too—you want to design an experiment that produces the evidence most likely to substantially update your priors—but I think “choose right direction for new AI paradigm” is more a m\_direction question, and the more important thing to get right in a taste-only singularity.

I combine m\_dir and m\_exp via weighted arithmetic mean: m\_eff \= w · m\_dir \+ (1 − w) · m\_exp  
where “w” is the weighting of m\_direction. I calculate estimates of taste-only singularity at w \= 0.3, 0.5, and 0.7. 

I keep m\_dir at Eli’s implicit value of 0.24 rather than raise it a slight arbitrary amount. m\_exp I set at 0.615 based on TasteVal’s finding that (given a problem) experimental taste doubles every 4.6 points of ECI.

Against Eli’s β \= 0.327, m\_eff is all the way at 0.615 with just TasteVal’s m\_exp \= m\_eff, but m\_eff drops with w dragging it back down toward Eli’s 0.24: w=.3 \-\> m\_eff \= .5, .5 \-\> .43, .7 \-\> .35.

Probabilities of taste-only singularity: w \= 0.3/0.5/0.7 gives 71/65/55% from 300-sample Monte Carlo runs on Eli’s distribution. (Recall that 37% is Eli default)

[^1]:  Summary of changes [here](https://www.lesswrong.com/posts/Gi4mzoupy2NqsoL7d/examining-ai-swarm-efficiency-with-the-ai-futures-model#Modifying_the_AI_Futures_Model), see full post for explanation/reasoning.

[^2]:  Although on some tasks I think λ \> 1 [will be measured in the future](https://www.lesswrong.com/posts/EnpJ29asosMKcFGL8/swarm-organization-as-the-exponent-on-test-time-compute#Conclusion), I’ve updated my estimate of “the fraction of tasks that benefit strongly from an agent swarm” lower recently. It’s notable that ex. recent OpenAI math results were *not* swarm-based and ex. that I still have limited use for multi-agent systems in professional software work.