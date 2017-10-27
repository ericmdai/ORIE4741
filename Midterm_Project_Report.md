# Project Midterm Report

## Authors: Jessie Wang ​(yw696), ​Anil ​Vadali (arv42)

## Abstract
With​ ​over​ ​ 600 ​ ​movies​ ​being​ ​made​ ​in​ ​the​ ​US​ ​each​ ​year​ ​and​ ​increasing​ ​competition​ ​from​ ​new
companies,​ ​the​ ​keys​ ​to​ ​film​ ​success​ ​has​ ​become​ ​more​ ​important​ ​than​ ​ever.​ ​As​ ​a​ ​result,​ ​in​ ​this​ ​project,​ ​we
hope​ ​to​ ​explore​ ​and​ ​predict​ ​what​ ​features​ ​of​ ​movies​ ​make​ ​them​ ​more​ ​successful​ ​than​ ​others.​ ​Specifically,
we​ ​are​ ​developing​ ​a​ ​model​ ​that​ ​will​ ​analyze​ ​and​ ​predict​ ​the​ ​IMDB​ ​score​ ​for​ ​a​ ​certain​ ​movie,​ ​which​ ​is​ ​the
baseline​ ​for​ ​how​ ​successful​ ​a​ ​film​ ​is​ ​in​ ​the​ ​movie​ ​world.

## Dataset ​Description

The​ ​original​ ​dataset​ ​has​ ​ 4803 ​ ​data​ ​points​ ​and​ ​ 22 ​ ​features​ ​in​ ​tmdb_5000_movies​.csv file ​and​ ​ 3 ​ ​features
in​ ​tmdb_5000_credits.csv file.
After​ ​data​ ​preparation,​ ​we​ ​ended up including​ ​the following features:​ ​budget,​ ​popularity,​ ​revenue,​ ​runtime,
status,​ ​vote_count,​ ​release_date_year,​ ​release_date_month,​ ​the​ ​first​ ​three​ ​genre​ ​IDs,​ ​the​ ​first​ ​three
keywords,​ ​the​ ​first​ ​three​ ​production_companies. For multiple label category features such as genre, keywords,
and production companies, we only included the first three values listed in order to standardize the category
for all movies. This is because some movies may have 1 genre associated with it, while others may have several 
and this variance may end up leading to some data sparsity issues and overall impact the final result. Additionally, 
the first three are indicative of the category as the data set places more important results higher in the list of attributes. For example, we 
believed that if Disney, LucasFilm, and Marvel were the first three production companies, they will be much more 
predictive of performance, over say the seventh production company which may have played a very small role in the 
creation of the film. 
The​ ​feature​s ​we​ ​discarded​ ​for​ ​midterm​ ​report​ ​included​ ​homepage,​ ​id,​ ​original​ ​language,​ ​title,
overview,​ ​tagline.​ ​We are discarding some of these features ​because​ ​we​ ​think​ ​they​ ​are​ ​irrelevant​ ​to​ ​the
prediction.​ ​These​ ​features​ ​include​ ​homepage​ ​url,​ ​id.​ ​We​ ​are​ ​also discarding​ ​original​ ​language​ ​because​ ​the
majority​ ​of​ ​them​ ​are​ ​in​ ​English​ ​and​ ​the​ ​sample​ ​for​ ​non-English​ ​movies​ ​are​ ​not​ ​big​ ​enough​ ​to​ ​give
reasonable​ ​insights​ ​into​ ​the​ ​data.​ ​Finally, we​ ​are​ ​discarding​ ​title,​ ​overview,​ ​tagline,​ ​etc​ ​for​ ​now​ ​because​ ​in​ ​order
to​ ​make​ ​use​ ​of​ ​these​ ​features,​ ​we​ ​need​ ​more​ ​advanced​ ​techniques​ ​such​ ​as​ ​NLP.

## Visualization ​of ​Potential ​Important ​Data ​Features

__Histogram​ ​of​ ​average​ ​rating__:​ ​The​ ​histogram​ ​gives​ ​us​ ​a​ ​visualization​ ​representation​ ​of​ ​the​ ​voting​ ​average
range.​ ​As​ ​we​ ​can​ ​see,​ ​the​ ​histogram​ ​gives​ ​a​ ​bell​ ​shaped​ ​data,​ ​which​ ​means​ ​the​ ​vote_average​ ​of​ ​all
movies​ ​are​ ​pretty​ ​close​ ​to​ ​normal​ ​distribution.

[Ratings Histogram](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image5.png)

__Line​ ​fit​ ​between​ ​rating​ ​and​ ​budget__:​ ​The​ ​left​ ​graph​ ​is​ ​the​ ​scatter​ ​plot​ ​of​ ​vote_average​ ​vs.​ ​budget
(vote_average​ ​as​ ​the​ ​y​ ​axis​ ​and​ ​budget​ ​as​ ​the​ ​x_axis),​ ​which​ ​gives​ ​us​ ​a​ ​general​ ​idea​ ​of​ ​the​ ​data
distribution.​ ​The​ ​right​ ​graph​ ​is​ ​an​ ​attempt​ ​to​ ​fit​ ​a​ ​linear​ ​model,​ ​which​ ​shows​ ​slight​ ​correlation​ ​between
vote_average​ ​and​ ​budget.

[Ratings vs. Budget Scatterplot](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image1.png)

[Ratings vs. Budget Trendline](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image2.png)

__Line​ ​fit​ ​between​ ​popularity​ ​and​ ​rating__:​ ​The​ ​graph​ ​on​ ​the​ ​left​ ​is​ ​the​ ​scatter​ ​plot​ ​of​ ​the​ ​popularity​ ​ratings​ ​for
each​ ​movie​ ​in​ ​the​ ​dataset​ ​we​ ​analyzed​ ​and​ ​it​ ​is​ ​compared​ ​against​ ​what​ ​rating​ ​the​ ​movie​ ​ended​ ​up​ ​getting
(popularity​ ​score​ ​on​ ​the​ ​x-axis​ ​vs.​ ​voting​ ​average​ ​on​ ​the​ ​y-axis).​ ​We​ ​originally​ ​believed​ ​that​ ​the​ ​popularity
feature​ ​would​ ​play​ ​a​ ​large​ ​role​ ​in​ ​determining​ ​the​ ​overall​ ​movie​ ​rating​ ​score​ ​since​ ​a​ ​movie​ ​that​ ​is​ ​often
times​ ​more​ ​popular,​ ​is​ ​generally​ ​admired​ ​more.​ ​As​ ​a​ ​result,​ ​we​ ​wanted​ ​to​ ​observe​ ​any​ ​trends​ ​between
these​ ​two​ ​fields.​ ​Though​ ​there​ ​appears​ ​to​ ​be​ ​a​ ​positive​ ​linear​ ​trend​ ​between​ ​the​ ​two​ ​variables,​ ​we​ ​later
realized​ ​that​ ​the​ ​popularity​ ​field​ ​is​ ​not​ ​very​ ​significant​ ​in​ ​the​ ​prediction​ ​of​ ​the​ ​overall​ ​score​ ​based​ ​on​ ​the
analysis​ ​described​ ​below. This may be due to the fact that this data field may be representing another 
facet of what we were believing, and thus needs further research.

[Ratings vs. Popularity Scatterplot](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image3.png)
[Ratings vs. Popularity Trendline](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image4.png)

__Missing/Corrupted​ ​Data__
After​ ​processing​ ​the​ ​data,​ ​we​ ​check​ed ​for​ ​missing​ ​data​ ​and​ found that ​they​ ​mainly​ ​existed​ ​in​ ​the​ ​genre_id,
keyword_id​ ​and​ ​production_company_ids​ ​because​ ​different​ ​movies​ ​have​ ​different​ ​number​ ​of​ ​associated
genre,​ ​keyword​ ​and​ ​production_company values.​ ​The​ ​way​ ​we​ ​are​ ​handling​ ​missing​ ​data​ ​is​ ​just​ ​to​ ​discard​ ​any
row​ ​with​ ​missing​ ​data,​ ​but​ ​this​ ​might​ ​be​ ​problematic​ ​since​ ​we​ ​only​ ​have​ ​ 3600 ​ ​data​ ​points​ ​for​ ​training​ ​and
many​ ​of​ ​them​ ​have​ ​at​ ​least​ ​one​ ​missing​ ​data.​ ​Another​ ​method​ ​we​ ​can​ ​use​ ​is​ ​to​ ​replace​ ​the​ ​missing
genre_id,​ ​keyword_id​ ​and​ ​production_company_id​ ​with​ ​the​ ​mode.​ ​We​ ​will​ ​experiment​ ​on​ ​different
methods​ ​and​ ​choose​ ​the​ ​one​ ​with​ ​lower​ ​validation​ ​error.
__CV__
For​ ​cross-validation,​ ​we​ ​decided​ ​to​ ​separate​ ​the​ ​entire​ ​data set​ ​into​ ​75%​ ​training​ ​and​ ​25%
validation​ ​data.​ ​We​ ​will​ ​also​ ​try​ ​LOOCV​ ​and​ ​k-fold​ ​for​ ​future​ ​analysis.

### Techniques to ​Avoid Over/Underfitting

1) Linear​ ​model​ ​with​ ​Regularizer​ ​(L1​ ​vs.​ ​L2)
2) Kernelized​ ​Linear​ ​Model
Since​ ​linear​ ​model​ ​is​ ​a​ ​very​ ​inflexible​ ​model​ ​that​ ​can​ ​easily​ ​underfit​ ​important​ ​patterns​ ​and​ ​cause
high​ ​bias,​ ​we​ ​want​ ​to​ ​use​ ​kernelized​ ​linear​ ​model​ ​to​ ​relax​ ​the​ ​strict​ ​linear​ ​assumption​ ​and​ ​try​ ​to​ ​decrease
the​ ​bias​ ​error​ ​to​ ​a​ ​reasonable​ ​value.
3) Decision​ ​Tree​ ​with​ ​Bagging
Since​ ​decision​ ​tree​ ​is​ ​a​ ​highly​ ​flexible​ ​model​ ​with​ ​a​ ​hard-to-find​ ​“sweet​ ​spot”​ ​that​ ​balances
reasonably​ ​low​ ​bias​ ​and​ ​reasonably​ ​low​ ​variance,​ ​we​ ​want​ ​to​ ​avoid​ ​overfitting​ ​to​ ​the​ ​training​ ​data​ ​by
applying​ ​bagged​ ​decision​ ​tree​ ​(random​ ​forest)​ ​and​ ​decision​ ​tree​ ​pruning.

## Preliminary ​Analysis

1) __Linear​ ​model__:​ ​For​ ​the preliminary​ ​analysis,​ ​we​ ​wanted​ ​to​ ​have​ ​a​ ​basic​ ​idea​ ​of​ ​how​ ​well​ ​a​ ​linear​ ​model
would​ ​fit​ ​to​ ​predict​ ​voting​ ​average.​ ​For​ ​simplicity​ ​reasons,​ ​we​ ​are​ ​only​ ​using​ ​numeric​ ​values​ ​for
this​ ​analysis​ ​and​ ​will​ ​incorporate​ ​categorical​ ​variables​ ​later.​ ​From​ ​the​ ​summary​ ​we​ ​get​ ​from​ ​fitting
this​ ​linear​ ​model,​ ​we​ ​can​ ​see​ ​that​ ​variables​ ​such​ ​as​ ​budget,​ ​runtime,​ ​vote_count​ ​have​ ​significant
contribution​ ​to​ ​prediction​ ​of​ ​voting​ ​average,​ ​X21​ ​(release​ ​date​ ​year)​ ​and​ ​X22(release​ ​date​ ​month)
also​ ​has​ ​somewhat​ high ​contribution.​ ​We​ ​also​ ​found​ ​the​ ​RSE​ ​is ​relatively​ ​low​ ​and​ ​Adj​ ​R^2​ ​is
relatively​ ​too​ ​high,​ ​which​ ​means​ ​this​ ​linear​ ​model​ ​is​ ​not​ ​enough​ ​to​ ​predict​ ​voting​ ​averages.​ ​We
will​ ​use​ ​other​ ​techniques​ ​and​ ​add​ ​more​ ​data​ ​features​ ​to​ ​make​ ​the​ ​model​ ​more​ ​accurate.

[Linear Model Analysis](https://github.com/ericmdai/ORIE4741/blob/master/Midterm%20Analysis%20Images/image6.png)

### Future Work

1) __Incorporate​ ​categorical​ ​variables__
We​ ​hope​ ​to​ ​approach​ ​utilizing​ ​categorical​ ​variables​ ​in​ ​many​ ​different​ ​ways.​ ​One​ ​specific
approach​ ​we​ ​could​ ​try​ ​is​ ​to​ ​use​ ​one-hot​ ​encoding​ ​to​ ​represent​ ​each​ ​categorical​ ​variable​ ​feature.
However,​ ​a​ ​main​ ​concern​ ​is​ ​that​ ​it​ ​may​ ​lead​ ​to​ ​a​ ​sparsity​ ​within​ ​vectors/matrices.​ ​This​ ​may​ ​lead​ ​to​ ​very
small​ ​weights​ ​overall​ ​for​ ​those​ ​features​ ​at​ ​the​ ​end.​ ​Additionally,​ ​another​ ​method​ ​we​ ​hope​ ​to​ ​explore​ ​is​ ​to
utilize​ ​some​ ​variant​ ​of​ ​NLP​ ​to​ ​analyze​ ​the​ ​text​ ​features.​ ​This​ ​would​ ​be​ ​another​ ​challenge​ ​that​ ​we​ ​may
have​ ​to​ ​encounter​ ​in​ ​the​ ​future.
2) __Add​ ​regularizer​ ​to​ ​the​ ​linear​ ​model__
3) __Implement​ ​a​ ​RBF​ ​kernel​ ​linear​ ​model__
4) __Implement​ ​a​ ​Bagged​ ​Decision​ ​Tree__
5) __Incorporate​ ​Facebook​ ​Likes/Twitter​ ​Favorites/Youtube​ ​Views__
The​ ​latest​ ​dataset​ ​update​ ​removed​ ​the​ ​facebook​ ​likes​ ​feature.​ ​We​ ​will​ ​try​ ​to​ ​retrieve​ ​these
information​ ​if​ ​we​ ​can.​ ​Another​ ​option​ ​one​ ​of​ ​our​ ​proposal​ ​peer​ ​reviewers​ ​mentioned​ ​that​ ​may​ ​useful
would​ ​be​ ​to​ ​see​ ​how​ ​many​ ​views​ ​a​ ​certain​ ​movie​ ​trailer​ ​got​ ​on​ ​Youtube​ ​and​ ​utilize​ ​that​ ​information​ ​as​ ​a
feature​ ​as​ ​well.


