#-----------Import libraries-------------

import spacy

#----------constant variables-----------

nlp = spacy.load('en_core_web_md')
GREEN = '\033[92m'
BOLD = '\033[1m'
ENDC = '\033[0m'

#-----------default variables------------

#original_film_title and _description variables created for later use in message printed to user.
original_film_title = "Planet Hulk"
original_film_description = nlp('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.')
#movie_titles, _descriptions & similarity_scores variables set up as default lists for later use.
movie_titles = []
movie_descriptions = []
similarity_scores = []

#-----------Custom Function---------------

def movie_recommendation(film):

    movie_titles = []
    movie_descriptions = []
    similarity_scores = []

    #opened movies.txt in read only
    file = open("movies.txt", "r")
    #created temporary file for the raw list version of txt file for manipulation.
    movie_temp = file.readlines()
    #closed file after use.
    file.close()

    #Created for loop to do following:
    #-Add titles of films to movie_titles variable list.
    #-add descriptions, with new line code removed on each, to movie_descriptions variable list.
    for line in movie_temp:
        temp_line = line[0:7]
        movie_titles.append(temp_line)
        temp_line = line[9:]
        temp_line = temp_line.strip("\n")
        movie_descriptions.append(temp_line)
    #created list of similarity scores between original film watched and potential films
    for token in movie_descriptions:
        token = nlp(token)
        score = film.similarity(token)
        similarity_scores.append(score)

    #created starting similarity score of 0 to then be compared to each value in list above.
    similarity_scores_value = 0
    #Compared each similarity score for each film in the movies.txt list with 0 followed by every other score from the list.
    for x in similarity_scores:
        if x > similarity_scores_value:
            similarity_scores_value = x
    #found the indexed position of the highest score.
    index = similarity_scores.index(similarity_scores_value)

    print(f"\n{BOLD}We would recommend the following film -{ENDC}"
        f"\n{GREEN}{movie_titles[index]}:"
        f"\n{movie_descriptions[index]}{ENDC}")

#-----------Program-------------------

#displayed neat recommendation text based on the indexation of the similarity score in relation to both title and description lists.
print(f"\n{BOLD}Based on your last watched film -{ENDC}"
      f"\n{original_film_title}:"
      f"\n{original_film_description}")

movie_recommendation(original_film_description)