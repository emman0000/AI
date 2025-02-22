# Q2

## **Playing a Decent Game of Table Tennis**  
**<span style="color:red;">🔴 Not Feasible</span>**  

Historical context elucidates that the world began to see tennis-playing robots in the late 90s. An early model, **Ttmatc-101**, graced German catalogues in 1976. Since their debut more than half a century ago, these robots can put up a rigorous fight against most beginner-level players with little to no knowledge. However, even the most recent developments as late as just this previous year seem to decline significantly as the opponents’ experience increases.  

A decent game between average players of an amateur level can lead to the ping-pong ball reaching speeds over **100 mph**, rendering matching the skill level of anyone above the beginner level of the game an obstacle yet to be tackled.  

In terms of the technical limitations, the aforementioned fast-paced nature of the sport demands **swift perception paired with impeccable motor control**, governed by rapid decision-making. Consequently, replicating these human abilities in robots is complex due to **limitations in sensor technology, processing speed, and mechanical dexterity**.  

---

## **Playing a Decent Game of Bridge at a Competitive Level**  
**<span style="color:red;">🟢 Feasible</span>**  

According to *The Guardian* in an article published in March 2022, an AI agent known as **NooK** defeated **eight world champions** at bridge. Since bridge is a skill-based game, the AI was trained on different plays and was able to learn over time, much like human learning patterns.  

---

## **Writing an Intentionally Funny Story**  
**<span style="color:red;">🔴 Not Feasible</span>**  

There have been attempts to create AI agents and models that can generate comedic elements, such as **Jon the Robot**. However, this particular branch, full of potential, is still in its infancy, primarily due to the **nature of comedy itself**.  

Comedy is heavily subjective; it is a product of **culture and various nuances** that are so hard to perfect that even accomplished comedians can face backlash. Conclusively, perhaps AI can always respond with a well-structured punchline if one demands it, but it's safe to say that **behind every punchline is an actual person** who has deemed it funny for the program running the AI itself.  

---

## **Giving Competent Legal Advice in a Specialized Area**  
**<span style="color:red;">🔴 Not Feasible</span>**  

AI has yet to shine in fields that require **out-of-the-box thinking**. Legal advice in specialized cases is heavily incumbent on professional individuals who **not only know the law of their jurisdiction but are also well-versed in loopholes and reading between the lines** to benefit clients. This is something AI has little mastery over.  

---

## **Discovering Mathematical Theorems**  
**<span style="color:red;">🔴 Not Feasible</span>**  

Ironically, even though AI is built upon mathematics, **math stems from abstract thinking** and analyzing the nature of phenomena to come to logical conclusions—something so far only the **human mind is capable of**.  

---

## **Performing a Surgical Operation**  
**<span style="color:red;">🟠 Feasible and Not Feasible</span>**  

Human life is precious, and leaving it **completely** in the hands of a machine will always pose risks, regardless of the machine's efficacy rate. AI is already assisting surgeons in the **operating room**, but human supervision is something that will perhaps never be eradicated from the health sector.  

Quick **decision-making skills and adaptability** in unexpected situations remain **unique to the human brain**, making full automation infeasible for now.  

---

## **Unloading Any Dishwasher in Any Home**  
**<span style="color:red;">🔴 Not Feasible</span>**  

AI-powered dishwashers for home use exist, but they do **not manually unload dishes**. This is due to:  

- The **sheer cost and risk** of installing hardware that does not yet exist at a **commercially viable level**.  
- Variability in **kitchen layouts and dish arrangements**, making it difficult to develop a generalize

#  Q3
## **Domain : Stock Trading**

An interesting domain where automated trading bots can be used to not only process and analyse statistical and financial data but also predict the trend a particular market will follow. Consequently, a more trained and reliable version would also execute the purchasing or selling of stock.
## Stock Trading Environment Characterization

| **Property**      | **Stock Trading Environment** | **Explanation** |
|------------------|----------------------------|----------------|
| **Accessible**  | ❌ No (Inaccessible)       | The agent does not have complete information (e.g., insider trading data, future events). |
| **Deterministic?** | ❌ No (Stochastic)         | Stock prices are affected by unpredictable factors like news, investor behavior, and economic events. |
| **Episodic?**    | ❌ No (Sequential)         | Each trade affects future decisions (e.g., holding or selling stocks later depends on previous trades). |
| **Static?**      | ❌ No (Dynamic)            | Stock prices, market trends, and external factors constantly change in real-time. |
| **Continuous?**  | ✅ Yes (Continuous)       | Prices, trade volumes, and market trends change continuously rather than in fixed steps. |

### Summary
The **stock trading environment** is **inaccessible, stochastic, sequential, dynamic, and continuous**.  
A **learning-based agent** is best suited to handle this complex and unpredictable environment. This is so that the agent can familiarize itself with the dynamic nature of the market rather than rely on trends that almost always seem unreliable. 
However certain features for example the reaction to sudden changes would prove to be better governed by a **model-based reflex agent**.


# Q4
## **An agent that senses only partial information about the state cannot be perfectly rational**
False.

AI models depend on techniques such as fuzzy logic, probabilistic reasoning and many more powerful tools that enable them to navigate uncertainty. An interesting example is the Inventory management AI deployed at a leading US departmental store "WALMART"; their recent inventory model can accurately predict stock demand and reorder products considering certain trends' uncertainty.

## **There exist task environments in which no pure reflex agent can behave rationally**
True.

In the case of a more sophisticated environment, a reflex agent would prove moot. This is primarily because reflex agents only operate on an immediate percept reception scenario; they only take into account any current stimuli generated rather than a chain of events. For example, a game-playing agent that plays against an opponent in any skill-based game must keep track of previous plays to make an informed decision

## **There exists a task environment in which every agent is rational**
It is impossible to construct an environment where every agent is rational. Rationality is a property that depends on the agent's design, goals, and environment, and not all agents can meet these criteria simultaneously. For instance, an agent that is engaged in a game of tic tac toe; n tic-tac-toe, if both players are perfectly rational and play optimally, the game will always end in a draw. However, this is a very specific and idealized scenario. In reality, not all agents will be perfectly rational, and the presence of irrational agents is what makes the game dynamic and interesting.

 ## **The input to an agent program is the same as the input to the agent function**
 False.
 
 A function is structured logically to perceive the input. The function is an aspect of the overall program so while it may only provide one desired outcome, the program itself might be engaged in maintaining other features that complement the function and the overall output of the software/hardware. A Thermostat agent for example may have a function that turns the heat up and down according to the environment. On the other hand, the entirety of the program may simultaneously be engaged in timing the cooling system, managing the efficiency etc.

 ## **Every agent function is implementable by some program/machine combination**
False.

Some agent functions may require infinite memory or computational resources, making them impractical or impossible to implement. An agent that perfectly predicts stock market prices would need unlimited computational power, which is infeasible.

## **Suppose an agent selects its action uniformly at random from the set of possible actions. There exists a deterministic task environment in which this agent is rational**
True.

Imagine a scenario where an agent is tasked with selecting a number between 1 and 10, and the environment is designed such that no matter which number the agent chooses, the outcome is always the same (e.g., the agent always receives a fixed reward). In this case, since every action leads to an identical result, selecting a number uniformly at random is a rational strategy. There’s no advantage to choosing one number over another, so randomness doesn’t harm the agent’s performance, and it aligns perfectly with the environment’s deterministic nature. There are certain card games where the dealer always wins a share regardless of the outcome for other players a real-life situation partially similar to this one.

## **It is possible for a given agent to be perfectly rational in two distinct task environments.**
True.

If an agent chooses its action randomly from all possible options, there exists a deterministic task environment where this behaviour is rational. In such environments, the outcome is fixed regardless of the agent's choice, making random selection a perfectly reasonable strategy since no action provides an advantage over another
