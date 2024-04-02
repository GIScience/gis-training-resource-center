# How to teach GIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

<!--This article will focus on best practices for teaching GIS.
[not needed since it's said below again]--> 

Learning GIS can be challenging, especially for individuals who are new to the topic or have limited experience with technology beyond standard office systems. The concept of geodata and everything that it entails is quite removed from the things many people work on day to day in the humanitarian sector. However, to grasp these concepts is essential to work effectively with GIS and solve problems. That being said, often there is not enough time to dive deep into topics like projections or algorithms. And we lean more through practical hands-on training than lectures about GIS theory.

This is why we must be aware of balancing practical hands-on and theory when teaching GIS. 
In the following article, we will present best practices for teaching GIS according to our experiences. We will start with overarching topics [such as](!!!). The further we progress, the further we will dive into practical things to do when teaching GIS.

<!--ADD: rewrite the last two sentences-->


## Theory vs. Hands-on

In general, we want to teach GIS in a way that people understand how they can do specific things needed in their work in the easiest way possible. This means we focus on practical exercises with a real-world connection so it is easy for people to see how they can use GIS in their work. However, sometimes we need to teach things theoretically. Usually, because they are either so essential people have to understand the concept before doing anything in GIS e.g. the layer concept. Or, not knowing the concept results in errors and problems when working with GIS and geodata e.g. projections. 

Balancing theory and hands-on practice is essential in GIS training. Below, we outline some good practices for incorporating both aspects effectively:

* Make the trainees understand why it is important to understand the concept (e.g. avoiding mistakes and wrong results or being able to work much faster). For example, if they work with geodata that is projected in different coordinate reference systems.
* Use graphics, videos and other mediums to explain the concept. For example, to teach the topic of projections in module 1, we use videos and graphics. You can even bring a paper model and [demonstrate](https://education.nationalgeographic.org/resource/the-cartographers-dilemma/) the concept example.
```{dropdown} Projection demonstration: The Cartographer's Dilemma
%%html
<iframe src="https://res.cloudinary.com/dtpgi0zck/video/upload/q_auto/vc_vp9/v1/videos/The%20Cartographer's%20Dilemma.webm?_s=vp-1.10.1" width="750" height="500"></iframe>
```
* Make the connection from the theory to the practical use of GIS. For example, show what kind of errors using a wrong projection can create and why projections like UTM are important to use, or the difference between metric and geographic coordinate systems (for example, when using meters or kilometers when creating buffers). 

## GIS for tackling real-world problems

In the fast-paced world of humanitarian aid, time is a precious commodity, and the need to assist those in need directly is paramount. The motivation of trainees is highly dependent on them seeing the value GIS can bring to their daily work. That is why we always should work with real-life examples, data and exercises. Abstract exercises are not as effective as real-world ones as trainees will not understand the relevance of the methods and workflows in the exercise. 

This topic is reflected on the whole platform. The principal section dealing with the topic is "[Module 1: Examples of GIS used by humanitarian organisations](https://giscience.github.io/gis-training-resource-center/content/Modul_1/en_qgis_theorie.html#examples-of-gis-used-by-humanitarian-organisations)".

On this training platform, nearly all exercises are oriented on methods, workflows or products that are standard in the humanitarian sector like overview maps or maps of affected regions. 

Practical tips to make exercise and teaching relevant for humanitarian work:
* __Audience:__ Reflect on your audience and think about what kind of products they would need the most.
* __Common products:__ In the beginning, go with easy map products for reports and presentations. In our experience that is interesting for everybody since everybody needs to present and report their work in reports or proposals.
* __Scenarios:__ Customize the exercises to simulate scenarios commonly encountered in humanitarian work, such as creating situational maps for emergency response teams or analyzing spatial data to identify high-risk areas.
* __Real datasets:__ Encourage trainees to explore real datasets and develop GIS solutions for actual humanitarian challenges, fostering hands-on learning and problem-solving skills.
* __Success stories:__ Utilize case studies or success stories from organizations such as on [Reliefweb](https://reliefweb.int) to illustrate the tangible impact of GIS in humanitarian operations, inspiring trainees and reinforcing the value of their training.
* __Fulfilling a mission:__ Present instances where GIS has been instrumental in fulfilling a mission.
* __Planning process:__ Empower trainees by involving them in the curriculum planning process, allowing them to identify the types of maps and products most relevant to their work.


## Hands-on exercises

Hands-on exercises are highly effective when teaching GIS on all skill levels. From exploring the interface to running a whole spatial analysis, doing these tasks gives people a better understanding how to work with GIS. It is always recommended to use hands-on exercises above theoretical presentations.

There are two very common types of hands-on training: Follow-along exercises and group exercises. 

::::{grid} 2
:::{card} Follow-along exercises
Follow-along exercises are a great tool to introduce new tools and functions because the trainer is directly there to answer questions and help solve problems.

```{list-table}
:header-rows: 1

*   - Advantages 
    - Disadvantages
*   - `+` Good to introduce new topics
    - `-` Limited exchanges between trainees
*   - `+` Questions can be answered immedialty
    - `-` Not a lot of initiative can be taken by trainees
*   - `+` Good problem-solving possibilites by trainers
    - 
```
:::

:::{card} Group exercises
Group exercises rely more on the independent work of the trainees. This is great for fostering discussions and exchange among the trainees. 

```{list-table}
:header-rows: 1

*   - Advantages 
    - Disadvantages
*   - `+` Great exchange between trainees
    - `-` No immediate support by the trainer(s)
*   - `+` Initiative and collaborative problem-solving are fostered
    - 
*   - `+` Great for training rather than the introduction of new things
    - 
```

:::
::::


### Beginning of an exercise 

Independent from the type of exercise, you should briefly go over the following points with the trainees at the beginning of the exercise:

1. __Aim of the exercise:__ In general, a hands-on exercise should start with explaining the goal of the exercise. For example: _„This exercise aims to teach the process of basic spatial data processing using the tools Clip, Merge and dissolve."_ This is a good opportunity to highlight the practical use of the tools the participants will learn to boost motivation.
2. __Background:__ Ideally, the exercise is built around a real-world example or a fictional scenario within the humanitarian work. In this case, you should quickly explain the background and story. An example of this is the exercise.
<!---ADD: insert example exercise-->
3. __Exercise Data:__  Most hands-on exercises use real-world data (from [HDX](https://data.humdata.org), for example). Each dataset used in the exercise should be explained shortly. This information can be found on each exercise on the platform. Make sure that everybody has downloaded the exercise data before you start. Note that some trainees are not familiar with `zip.` files. Make sure the trainees unzip the folders before trying to import them into QGIS and take the time to solve any other issues concerning the exercise data. 

### During the exercise: Follow-along
If you run a follow-along exercise, you can follow these basic principles for going through the exercise. Explain the purpose of each step. E.g. _„In this step we load the data into QGIS“_ or _„In this step, we cut out all points expat the ones in the area of interest“_. Expect to show every step three times. Either on a large screen or by sharing your screen (remote). For this, you might need to have a lot of patience. People will need to switch between watching you perform the steps on your screen and orienting themselves in the QGIS interface on their own computer to perform the steps. This will take a lot of time and there is no sense in rushing things. The goal of the workshop is to not leave anybody behind. Be very deliberate and show everything step by step, even very small things. You might have to ask several times if there are any issues. 

```{tip} Do not use icon buttons! 
Use the tabs or the geoprocessing toolbox as much as possible rather than clicking on icons. Seeing icons can be hard for participants but searching for tools in the processing toolbox is much easier.
```

1. During the first demonstration encourage the trainees to just watch what you are doing. Do this slowly and deliberately.
2. In the secound demonstration let the trainees follow along on their computers.
3. The third demonstration can be used to address problems some of the participants might encounter during the secound demonstration. Sometimes it is worthed to give the trainees some time to explore different options. For example during tasks that have to do with styling of layers or maps. 

Once everybody has managed to produce the desired results, you can move on.

### During the exercise: Group work
In case you doing group work there are some other things to look out for. 
1. Sort all trainees into groups after you have done the introduction to the exercise. During the introduction of group work, it is important to explain if and how the groups should present their results.
2. Once this is done, give them some time to organise themselves and go over the instructions. 
3. After some time you should check and go through the groups to see if there are any questions or misunderstandings. 
4. After the initial round, visit the groups if necessary. Ask if the groups need more time and adjust the times accordingly
5. Once the group work is over gather the trainees together. Check if there are any problems or questions.
6. Once this is done, let the groups present their results. 

### End of an exercise 
After an exercise, you should take some time to ask the participants if they found the exercise relevant and if they are happy with to complexity level. Reflect with the trainees again on the possible use case of the things they just learned. Encourage discussion among the trainees and plan some time for the participants to exchange their experiences.

## Practise problem-solving: What if you are stuck?

Working with GIS will always entail that there is one point where you do not know how to proceed. Picture yourself wanting to achieve a specific task e.g. displaying only certain parts of the attribute table on your print map.

In the vast realm of QGIS, mastering every function is impractical. Instead, developing problem-solving methods is an important skill when working with GIS.
The ability to navigate challenges, and knowing where and how to seek solutions, is fundamental in GIS. Any comprehensive GIS training should prioritize the development of this skill. Here, we explore strategies to empower your participants in problem-solving within QGIS.

* __Utilizing the IFRF GIS Training Plattform Wiki:__ Encourage trainees to take advantage of QGIS training resources on this platform!
* __Effective use of search engines like Google:__ Teach trainees how to formulate precise search queries using relevant keywords related to their specific problem. Emphasize the importance of including relevant GIS software names, error messages, and specific task descriptions to yield accurate search results.
* __Effective use of QGIS Documentation:__ Trainees should learn how to effectively navigate [QGIS documentation](https://docs.qgis.org/3.34/en/docs/user_manual/), including user manuals, tutorials, and FAQs. Teach them how to use keywords related to their specific problem to find relevant information and step-by-step guides within the QGIS documentation.
* __Engaging with QGIS user community:__ Introduce trainees to [online forums, Telegramm groups and communities](https://www.qgis.org/en/site/forusers/support.html) dedicated to QGIS users, such as the QGIS Community Forum and [QGIS subreddit](https://www.reddit.com/r/QGIS/). Encourage active participation in discussions, where they can seek advice from experienced users, share their experiences, and collaborate on problem-solving.
* __Exploring QGIS tutorial videos:__ Recommend trainees to explore tutorial videos specifically focused on QGIS available on platforms like YouTube. These videos often provide visual demonstrations of QGIS functionalities and troubleshooting techniques for common issues.
* __Leveraging QGIS chatbots and AI assistants:__ Introduce trainees to AI-powered assistants like ChatGPT, specifically trained to provide instant responses to QGIS-related queries and offer guidance on troubleshooting specific issues. Teach them how to interact effectively with these assistants to obtain relevant information and solutions tailored to QGIS.
* __Engaging with QGIS user groups:__ Encourage trainees to [join local or online QGIS user groups](https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups) and Surge Information Management Support (SIMS) Geo group on Slack. In these communities they can connect with other QGIS users, mentors, and experts. Participating in user groups provides opportunities for networking, knowledge exchange, and mentorship in QGIS.




## Common mistakes, problems and hurdles

People new to GIS often fall over the same stumbling blocks. Each GIS application has its typical challenges and mistakes. In the process of teaching GIS, it's important to anticipate these common pitfalls to quickly address trainees' hurdles. 
Typical problems can be mishandling shapefiles, not seeing data on the map canvas because the order of layers is wrong, or using the wrong tool becaus of similar names (e.g. `Join by location` and `Join by location (summary)`). 

As a seasoned GIS user, you might avoid these mistakes automatically and don’t think about them often. Apprentice GIS users lack this experience. 

To deal with such issues you can follow the tips below:

* __Wiki:__ Point trainees to a curated [list of common problems and solutions](/content/Wiki/en_qgis_common_errors_and_Issues.md) available on the training platform, serving as a valuable reference resource.
* __Google and ChatGPT:__ Encourage trainees to use online resources like Google and utilize ChatGPT for additional problem-solving assistance, strengthening self-reliance and resourcefulness.
* ___Be proactive:__ When conducting exercises, proactively flag potential issues and provide step-by-step guidance to preemptively address trainees' concerns.
* __Collaborative learning:__ Foster a collaborative learning environment where trainees can share their experiences and solutions to common problems, promoting peer-to-peer support and knowledge sharing.
* __Breakout rooms:__ Consider utilizing breakout rooms for one-on-one troubleshooting sessions. This allows trainers to address individual challenges without disrupting the larger group. Be aware that the follow-along exercise might continue in the main room. Make sure the participants in the breakout room can catch up.
* __Best practices:__ Emphasize the importance of adhering to best practices in data management to mitigate common problems, highlighting the impact of proper data handling on GIS workflows, and their efficiency and accuracy.

By proactively addressing common mistakes and challenges in GIS training, you can empower your trainees to navigate the complexities of GIS effectively. Through collaborative problem-solving and adherence to best practices, we ensure a more fruitful and rewarding learning experience for all participants.
 
## Discussion and Groupwork

Discussion and groupwork play vital roles in GIS training, fostering collaboration, critical thinking, and knowledge exchange among participants. By engaging in discussions and collaborative activities, participants can deepen their understanding of GIS concepts and methodologies while also gaining valuable insights from their peers. The list below summarizes a few key reasons why discussion and groupwork are important in GIS training:

* __Exchange of ideas and perspectives:__ Group discussions provide opportunities for participants to share their experiences, insights, and perspectives on various GIS topics. This exchange of ideas enriches the learning environment and exposes participants to different approaches and problem-solving strategies.
* __Critical reflection:__ Group activities encourage participants to critically evaluate GIS methods, data sources, and analytical techniques. Through guided discussions and peer feedback, participants can assess the strengths and limitations of different approaches, enhancing their ability to make informed decisions in real-world GIS projects.
* __Learning from peers:__ Collaborative exercises and group projects enable participants to learn from each other's strengths and expertise. By working together to solve challenges and address complex problems, participants can learn diverse skill sets and knowledge backgrounds to achieve shared learning goals.
* __Enhanced engagement and participation:__ Groupwork promotes active learning and engagement, as participants collaborate on hands-on exercises, case studies, and project-based tasks. This interactive learning approach fosters a sense of ownership and accountability, motivating participants to actively contribute to the learning process.
* __Skill development:__ Through group activities, participants have opportunities to develop essential skills such as communication, teamwork, and problem-solving. These transferable skills are valuable not only in GIS but also in various professional contexts, enhancing participants' overall professional development.

Incorporating discussions and groupwork into GIS training sessions can create dynamic learning environments where participants can collaborate, learn from each other, and apply GIS concepts and skills in practical contexts.