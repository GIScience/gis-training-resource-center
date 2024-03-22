# How to teach GIS

This article will focus on best practices for teaching GIS. 

Learning GIS can be challenging, especially for individuals who are new to the topic or have limited experience with technology beyond standard office systems. The concept of geodata and everything that it entails is quite removed from the things many people work on day to day in the humanitarian sector. To grasp these concepts is however essential to work effectively with GIS and solve problems. That being said, often there is not enough time to dive deep into topics like projections or algorithms. And we lean more towards practical hands-on training.

That is why we must be aware of balancing practical hands-on and theory when teaching GIS. 
In the following, we will present best practices for teaching GIS according to our experiences. We will start with overarching topics. The further we progress, the further we will dive into practical things to do when teaching GIS.


## Theory vs. Hands-on

In general, we want to teach GIS in a way that people understand how they can do specific things in the easiest way possible. This means we focus on practical exercises with a real-world connection so it is easy for people to see how they can use GIS in their work. However, sometimes we need to teach things theoretically. Usually, because they are either so essential people have to understand the concept before doing anything in GIS e.g. the layer concept. Or, not knowing the concept results in errors and problems when working with GIS and geodata e.g. projections. 

Balancing theory and hands-on practice is essential in GIS training. Here, we outline best practices for incorporating both aspects effectively:

* Make the trainees understand why it is important to understand the concept. E.g. avoiding mistakes and wrong results or being able to work much faster. For example, if they work with geodata that is projected in different coordinate reference systems.
* Use graphics, videos and other mediums to explain the concept. For example, to teach the topic of projections in Modul 1 we use videos and graphics. You can even bring a paper model and [demonstrate](https://education.nationalgeographic.org/resource/the-cartographers-dilemma/) the concept example.
```{dropdown} Projection demonstration: The Cartographer's Dilemma
%%html
<iframe src="https://res.cloudinary.com/dtpgi0zck/video/upload/q_auto/vc_vp9/v1/videos/The%20Cartographer's%20Dilemma.webm?_s=vp-1.10.1" width="750" height="500"></iframe>
```
* Make the connection from the theory to the practical use of GIS. For example, show in what kind of errors a wrong projection can result and why projections like UTM are important to use meters and kilometres when for example buffering.

## GIS for tackling real-world problems

In the fast-paced world of humanitarian aid, time is a precious commodity, and the need to assist those in need directly is paramount. The motivation of trainees is highly dependent on them seeing the value GIS can bring to their daily work. That is why we always should work with real-life examples, data and exercises.  Abstract exercises are not as effective as real-world ones. 

This topic is reflected on the whole platform. The principal section dealing with the topic is [Modul 1: Examples of GIS used by humanitarian organisations](https://giscience.github.io/gis-training-resource-center/content/Modul_1/en_qgis_theorie.html#examples-of-gis-used-by-humanitarian-organisations).

On this training platform, nearly all exercises are oriented on products that are standard in the humanitarian sector like overview maps or maps of affected regions. 

Practical tips to make exercise and teaching relevant for humanitarian work:
* Reflect on your audience and think about what kind of products they would need the most.
* In the beginning, go with easy map products for reports and presentations. In our experience that is interesting for everybody since everybody needs to present and report their work in reports or proposals.
* Customize exercises to simulate scenarios commonly encountered in humanitarian work, such as creating situational maps for emergency response teams or analyzing spatial data to identify high-risk areas.
* Encourage trainees to explore real datasets and develop GIS solutions for actual humanitarian challenges, fostering hands-on learning and problem-solving skills.
* Utilize case studies or success stories from organizations like Relifeweb to illustrate the tangible impact of GIS in humanitarian operations, inspiring trainees and reinforcing the value of their training.
* Present instances where GIS has been instrumental in fulfilling a mission.
* Empower trainees by involving them in the curriculum planning process, allowing them to identify the types of maps and products most relevant to their work.


## Hands-on exercises

Hands-on exercises are highly effective when teaching GIS on all skill levels. From exploring the interface to running a whole spatial analysis, doing these things gives people a lot of understanding of how to work with GIS. It is always recommended to use hands-on exercises above theoretical presentations.

There are two very common types of hands-on training: Follow-along exercises and group exercises. 

::::{grid} 2
:::{card} Follow-along exercises
Follow-along exercises are a great tool to introduce new tools and functions because the trainer is directly there to answer questions and help solve problems.

| Advantages  |  Disadvantages |
|---|---|
|+ Good to introduce new topics|- Limited exchanges between trainees|
|+ Questions can be answered immediately |- Not very much initiative by trainees|
|+ Good problem-solving possibilities by trainers| |
:::

:::{card} Group exercises
Group exercises rely more on the independent work of the trainees. This is great for fostering discussions and exchange among the trainees. 

| Advantages  |  Disadvantages |
|---|---|
|+ Great exchange between trainees|- No imidate support by the trainer|
|+  Initiative and collaborative problem-solving are fostered| |
|+ Great for training rather than the introduction of new thinks|  |
:::
::::


### Beginning of an exercise 

Independent from the type of exercise you should briefly go over the following points with the trainees at the beginning of the exercise:

1. __Aim of the exercise:__ In general, a hands-on exercise should start with explaining the goal of the exercise. For example _„this exercise aims to teach the process of basic spatial data processing using the tools Clip, Merge and dissolve."_ This is a good opportunity to highlight the practical use of the tools the participants will learn to boost motivation.
2. __Background:__ Ideally, the exercise is built around a real-world example or a fictional scenario within the humanitarian work. In this case, you should quickly explain the background and story. An example of this is the exercise.
3. __Exercise Data:__  Most hands-on exercise uses real-world data for example from HDX. Each dataset used in the exercise should shortly be explained. This information can be found on each exercise on the platform. Make sure that everybody can download the exercise data. Note that some trainees are not familiar with zip. files.

### During the exercise: Follow-along
If you run a follow-along exercise you can follow these basic principles for going through the exercise. Explain the purpose of each step. E.g _„In this step we load the data into QGIS“_ or _„In this step, we cut out all points expat the ones in the area of interest“_. Expect to show every step three times. Either on a large screen or by sharing your screen (remote). For this, you need to have a lot of patience. People will need a lot of time and there is no sense in rushing things. Be very deliberate and show everything step by step, even very small things. 

```{tip} Do not use icon buttons! 
Use the tabs or the geoprocessing toolbox as much as possible rather than clicking on icons. Seeing icons can be hard for participants but searching for tools in the processing toolbox is much easier.
```

1. During the first demonstration encourage the trainees to just watch what you are doing. Do this slowly and deliberately.
2. In the secound demonstration let the trainees follow along on their computers.
3. The third demonstration can be used to address problems some of the participants might encounter during the secound demonstration. Sometimes it is worthed to give the trainees some time to explore different options. For example during tasks that have to do with styling of layers or maps. 

Once everybody has managed to produce the desired results, you can move on.

### During the exercise: Group work
In case you doing group work there are some other things to look out for. Sort all trainees into groups after you have done the introduction to the exercise. During the introduction of group work, it is important to explain if and how the groups should present their results.
Once this is done, give them some time to organise themselves and go over the instructions. After some time you should make a round through the groups to see if there are any questions or misunderstandings. After the initial round trough, the groups do more visits as necessary. 
Check if the groups need more time and adjust the times accordingly.

Once the group work is over gather the trainees. Check if there are any problems or questions. Once this is done, let the groups present their results. 

### End of an exercise 
After an exercise, you should take some time to ask the participants if they found the exercise relevant and if they are happy with to complexity level. Reflect with the trainees again on the possible use case of the things they just learned. Encourage discussion among the trainees and plan some time for the participants to exchange their experiences.

## Common mistakes and problems

People new to GIS often fall over the same stumbling blocks. Each GIS application has its typical challenges and mistakes. In the process of teaching GIS, it's crucial to anticipate these common pitfalls to swiftly address trainees' hurdles. 
Typical problems can be mishandling shapefiles. Not seeing data on the map canvas because the order of layers is wrong or using the wrong tool becaus of similar names e. g. `Join by location` and `Join by location (summary)`. 

As a seasoned GIS user, you might avoid these mistakes automatically and don’t think about them often. Apprentice GIS users lack this experience. 

To deal with such issues you can follow the tips below:

* Point trainees to a curated [list of common problems and solutions](/content/Wiki/en_qgis_common_errors_and_Issues.md) available on the training platform, serving as a valuable reference resource.
* Encourage trainees to leverage online resources like Google and utilize ChatGPT for additional problem-solving assistance, fostering self-reliance and resourcefulness.
* When conducting exercises, proactively flag potential issues and provide step-by-step guidance to preemptively address trainees' concerns.
* Foster a collaborative learning environment where trainees can share their experiences and solutions to common problems, promoting peer-to-peer support and knowledge sharing.
* Consider utilizing breakout rooms for one-on-one troubleshooting sessions, allowing trainers to address individual challenges without disrupting the larger group.
* Emphasize the importance of adhering to best practices in data management to mitigate common problems, highlighting the impact of proper data handling on GIS workflows' efficiency and accuracy.

By proactively addressing common mistakes and challenges in GIS training, we empower trainees to navigate the complexities of GIS effectively. Through collaborative problem-solving and adherence to best practices, we ensure a more fruitful and rewarding learning experience for all participants.
 
