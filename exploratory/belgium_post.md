# 🇧🇪 Exploring data from the 2025 Belgian GP

The 2025 Belgian GP is the first live GP weekend since I started this project. And it's a tricky GP to have as the first one to analyze because it's not a regular F1 weekend: it's Sprint weekend. To understand what a Sprint weekend is, first we need to look at how a regular F1 weekend is structured:

**Regular F1 Weekend Structure**

| Session         | Duration                      | Description                                  |
| --------------- | ----------------------------- | -------------------------------------------- |
| Free Practice 1 | 60 minutes                    | Practice                                     |
| Free Practice 2 | 60 minutes                    | Practice                                     |
| Free Practice 3 | 60 minutes                    | Practice                                     |
| Qualifying      | ~60 minutes                   | Determines the start order grid for the race |
| Race            | 320 km (usually ~100 minutes) | The big event                                |

**Sprint**

In 2021 F1 introduced _sprint races_, a concept very common in lower formulae but a novelty in F1 introduced to attract more attention. The sprint race is just a shorter race (1/3 length of a feature race) run on Saturday.

Having another race means having another qualifying session. The total available time in the weekend is the same, which means 2 free practices need to be dropped during these type of weekends to make way for the new events.

**Sprint F1 Weekend**

| Session           | Duration                      | Description                                            |
| ----------------- | ----------------------------- | ------------------------------------------------------ |
| Free Practice 1   | 60 minutes                    | Practice                                               |
| Sprint Qualifying | ~45 minutes                   | Determines the start grid order for the _sprint_ race  |
| Sprint            | 1/3 feature race              | _Sprint_ race                                          |
| Qualifying        | ~60 minutes                   | Determines the start grid order for the _feature_ race |
| Race              | 320 km (usually ~100 minutes) | The big event                                          |

> On sprint weekends, teams have only 1 free practice to test what they usually do in 3 practices, which makes this forecasting project even trickier.

In reality, teams use the first half of the only practice to test tyre compounds and then switch focus (usually) to qualifying pace, as the first qualifying session is just a few hours after the practice.

In the sprint race, besides looking into getting more Championship points, teams gather race pace data for the big event on Sunday. This effectively makes the sprint race a sort-of second free practice for teams.
