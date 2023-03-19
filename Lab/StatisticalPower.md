## Statistical Power

Notes from lecture on March 13, 2023

### Definition

- The power of a planned experiment is the chance of getting a statistically significant result when a particular real treatment effect exists.
- It refers to the probability that we will correctly conclude that the treatment caused a change in the outcome.
- It is the probability of **accepting an alternative hypothesis, when the alternative hypothesis is true.**

Intuitively, it means that higher the power higher the probability of detecting an effect when there is an effect.

The **higher the statistical power** for a given experiment, **the lower the probability of making a Type II (false negative) error.** 

- **Low Statistical Power**: Large risk of committing Type II errors, e.g. a false negative.
- **High Statistical Power**: Small risk of committing Type II errors.

**Components**: 

— Effect Size, Significance level, Power, Sample Size.

- **Effect Size**. The quantified magnitude of a result present in the population. [Effect size](https://machinelearningmastery.com/effect-size-measures-in-python/) is calculated using a specific statistical measure, such as Pearson’s correlation coefficient for the relationship between variables or Cohen’s d for the difference between groups.
    - small, medium, large, and very large effect sizes for Cohen’s d are 0.20, 0.50, 0.80, and 1.3 respectively.
- **Sample Size**. The number of observations in the sample.
- **Significance**. The significance level used in the statistical test, e.g. alpha. Often set to 5% or 0.05.
- **Statistical Power**. The probability of accepting the alternative hypothesis if it is true.

**Uses:**

- **prior to an experiment**: the sample size needed to detect a particular effect can be estimated given different desired levels of significance, effect size, and power.
    - It is common to design experiments with a statistical power of 80% or better, e.g. 0.80. This means a 20% probability of encountering a Type II area.
- **validating** a study’s findings: Statistical power can be determined, by using the given sample size, effect size, and significance level, to help conclude whether the probability of committing a Type II error is acceptable from a decision-making perspective


**Ways to ensure sufficient power**

- Studying **sufficient numbers of subjects or a sample size**  is the most well known way to assure sufficient power.
- the main (partially) controllable experimental characteristic that affects power is **variability**. If you **can reduce variability, you can increase power.**
    - measurements variation
    - controlling environmental variation
    - subject-to- subject variablity
    - treatment Application


### Graphical Analysis
The following image demonstrates the effects of various factors on power, based on the experimental setup in chapter 12 of Seltman.
<img width="757" alt="Screen Shot 2023-03-13 at 1 08 25 PM" src="https://user-images.githubusercontent.com/39693183/224785765-a8f4268b-78f3-49f7-ad9f-aa54d7291f1c.png">


**Check the power analysis tutorial in Lab directory.**

--- 
References

[A Gentle Introduction to Statistical Power and Power Analysis in Python](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/)

Seltman, H. J. (2012). Experimental design and analysis. (Chapter 8 and chapter 12)
