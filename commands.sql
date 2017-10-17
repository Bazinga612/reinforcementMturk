# create table commands!
CREATE TABLE dialog_acts (dialog_act_id int NOT NULL PRIMARY KEY, dialog_act text);
CREATE TABLE starter (starter_id int NOT NULL PRIMARY KEY, utterance text);
CREATE TABLE mappings (mapping_id int NOT NULL PRIMARY KEY, starter_id int, dialog_act1_id int, dialog_act2_id int, dialog_act3_id int, dialog_act4_id int, FOREIGN KEY(starter_id) REFERENCES starter(starter_id), FOREIGN KEY(dialog_act1_id) REFERENCES dialog_act1(dialog_act1_id), FOREIGN KEY(dialog_act2_id) REFERENCES dialog_act2(dialog_act2_id), FOREIGN KEY(dialog_act3_id) REFERENCES dialog_act3(dialog_act3_id), FOREIGN KEY(dialog_act4_id) REFERENCES dialog_act1(dialog_act4_id));
CREATE TABLE dialog_act1 (dialog_act1_id int NOT NULL PRIMARY KEY, utterance text, name_act1 int, FOREIGN KEY(name_act1) REFERENCES dialog_acts(dialog_act_id));
CREATE TABLE dialog_act2 (dialog_act2_id int NOT NULL PRIMARY KEY, utterance text, name_act2 int, FOREIGN KEY(name_act2) REFERENCES dialog_acts(dialog_act_id));
CREATE TABLE dialog_act3 (dialog_act3_id int NOT NULL PRIMARY KEY, utterance text, name_act3 int, FOREIGN KEY(name_act3) REFERENCES dialog_acts(dialog_act_id));
CREATE TABLE dialog_act4 (dialog_act4_id int NOT NULL PRIMARY KEY, utterance text, name_act4 int, FOREIGN KEY(name_act4) REFERENCES dialog_acts(dialog_act_id));


#Dialog acts table commands
INSERT INTO dialog_acts VALUES (6, "Answer.rhetorical");
INSERT INTO dialog_acts VALUES (0, "Answer.negative");
INSERT INTO dialog_acts VALUES (7, "Answer.positive");
INSERT INTO dialog_acts VALUES (5, "Answer.elaboration");
INSERT INTO dialog_acts VALUES (4, "Answer.joking_sarcastic");
INSERT INTO dialog_acts VALUES (1, "Answer.TalkMore");
INSERT INTO dialog_acts VALUES (3, "Answer.continuation");
INSERT INTO dialog_acts VALUES (2, "Answer.change");


#Starter table commands
INSERT INTO starter VALUES (1, "I STILL think ""Monty Python and the Holy Grail"" is funny.") 
INSERT INTO starter VALUES (0, """The Wizard of Oz"" and ""Gone with the Wind"" were amazing at the time in part because of the color cinematography.") 


#Dialog acts1 table commands
INSERT INTO dialog_act1 VALUES (8, "Who can honestly say they don't know who Dorothy or the Tin Man is?  These movies are memorable for a reason!", 6);
INSERT INTO dialog_act1 VALUES (12, "Oh come on,  that movie is for nerds,  losers who live in their mom's basement.", 0);
INSERT INTO dialog_act1 VALUES (10, "I agree,  the color film was a game-changer at the time.", 7);
INSERT INTO dialog_act1 VALUES (4, "What do you like about these movies the best. The idea that they end on such a positive note all the time? I kind of like that too. Tell me why you like the endings?", 1);
INSERT INTO dialog_act1 VALUES (0, "I think these type of movies are overrated because they are old. Don't you think that is the reason they are so popular?", 0);
INSERT INTO dialog_act1 VALUES (13, "Some of their skits were pretty obscure due to their addictions I think.", 0);
INSERT INTO dialog_act1 VALUES (11, "Who wasn't blown away by these movies?", 6);
INSERT INTO dialog_act1 VALUES (7, "I really can't stand watching ""The Wizard of Oz.""  It was good when I was a kid,  but I grew out of it.", 0);
INSERT INTO dialog_act1 VALUES (5, "I don't think they look very good by today's standards,  of course.", 0);
INSERT INTO dialog_act1 VALUES (9, "I love ""The Wizard of Oz!""  There aren't many other movies that have the same longivity.", 7);
INSERT INTO dialog_act1 VALUES (2, "What do you think made ""Gone with the Wind"" seem authentic?", 1);
INSERT INTO dialog_act1 VALUES (1, "Yeah. What else did these films revolutionize about the industry?", 1);
INSERT INTO dialog_act1 VALUES (6, "I love movies like this. They are amazing. I wish I could see more like this in these days.", 7);
INSERT INTO dialog_act1 VALUES (3, "What do you think is the better movie? Its not cliche to ask if its Gone with the Wind or Wizard of Oz at all.", 6);


#Dialog acts2 table commands
INSERT INTO dialog_act2 VALUES (13, "I've never heard as much laughter in a movie theater as I did for that picture.", 5);
INSERT INTO dialog_act2 VALUES (7, "I think realism in today's films kind of make them bland. I think that's why Avatar was so popular,  because of how vibrant the characters were,  from a color standpoint.", 5);
INSERT INTO dialog_act2 VALUES (9, "Dorothy who?", 4);
INSERT INTO dialog_act2 VALUES (7, "That's the great thing about technicolor though! It's almost like modern art on film. The vibrancy is what makes it special.", 3);
INSERT INTO dialog_act2 VALUES (9, "There is a reason everyone knows who Judy Garland is,  that's for sure.", 3);
INSERT INTO dialog_act2 VALUES (2, "You mean other than how to stir up controversy?", 4);
INSERT INTO dialog_act2 VALUES (2, "You know,  say what you will about how they revolutionized the film industry,  but in both cases the books were better.", 2);
INSERT INTO dialog_act2 VALUES (7, "We always joke that you recognize an MGM musical more from the color than the soundtrack.", 4);
INSERT INTO dialog_act2 VALUES (6, "Do you remember the Carol Burnett Gone With the Wind sketch? Vicki Lawrence was pure gold in that.", 2);
INSERT INTO dialog_act2 VALUES (9, "Did you know at the time there was only two color cameras for shooting owned by the studio?", 2);
INSERT INTO dialog_act2 VALUES (10, "Well,  in the case of ""Gone with the Wind"" it was the first major motion picture to have a swear word in it.", 3);
INSERT INTO dialog_act2 VALUES (2, "The transition from black and white to color in Wizard of Oz really did draw the audience into the world of Oz. After reading the books,  I think this was probably the most profound way to do that in film.", 5);
INSERT INTO dialog_act2 VALUES (9, "Isn't it crazy to think they were being filmed at the same time?", 5);


#Dialog acts3 table commands
INSERT INTO dialog_act3 VALUES (4, "Yeah,  there was something so amazing about the witches and all of the different colors and the ruby slippers.", 5);
INSERT INTO dialog_act3 VALUES (9, "Well that's true. I remember ""bring forth the shrubbery"" the best.", 3);
INSERT INTO dialog_act3 VALUES (8, "I think all of the Monty Python moves are perfect for a game night.", 2);
INSERT INTO dialog_act3 VALUES (1, "I think it's amazing how memorable any transition is with technology,  it's like we'll always remember the very first smart phone,  the first laptop,  tablet,  3D movie... The Wizard of Oz was the first of it's kind just like those,  which is what made it so amazing.", 2);
INSERT INTO dialog_act3 VALUES (5, "It's like watching reality in fast forward what with all of the action scenes so close together.", 4);
INSERT INTO dialog_act3 VALUES (0, "I am in total agreement there. In most cases the movies pale in comparison to the books.", 3);
INSERT INTO dialog_act3 VALUES (6, "Yeah it's just so ""profound"" how sexist and degrading that movie is.", 4);
INSERT INTO dialog_act3 VALUES (2, "Remember when Harry Potter came out on film? I never liked the films near as much as I did the books. How can you fit a hole long book into an hour and a half?", 5);
INSERT INTO dialog_act3 VALUES (7, "Talking about fast paced movies,  I can't stand the animated movies that come out today. Call me slow but there's no way that I can keep track of all the stuff that's happening on screen.", 2);
INSERT INTO dialog_act3 VALUES (3, "I agree,  I loved seeing her step from her house into the colorful world... it was mesmerizing.", 3);


#Dialog acts4 table commands
INSERT INTO dialog_act4 VALUES (5, "Yeah,  although Dorothy herself seemed pretty mellow about it.", 4);
INSERT INTO dialog_act4 VALUES (9, "Books have a larger scope to show a story in though. They have as much or as little time as they need,  no constraints on budgets when it comes to a fantasy world or effects. Take Harry Potter,  the movies were huge,  effects,  just the whole thing all of them,  massive. But the books were somehow bigger.", 5);
INSERT INTO dialog_act4 VALUES (13, "That scene is funny. I really like all of the Monty Plython movies though. And the other ones are funny,  but not as well known as the Holy Grail.", 2);
INSERT INTO dialog_act4 VALUES (3, "The makeup was really good in The Wizard of Oz,  too. I mean it's not like modern horror movie stuff,  but the Scarecrow was really very effective,  especially for the time.", 5);
INSERT INTO dialog_act4 VALUES (1, "Do you remember how we used to get around in strange cities before we all had smartphones?", 2);
INSERT INTO dialog_act4 VALUES (12, "Monty Python some how can reach fifteen year old kids,  decades after its release and at the same time make a posh fifty year old laugh just as loud.", 5);
INSERT INTO dialog_act4 VALUES (10, "Right. COLOR TV! It's the FUTURE!", 4);
INSERT INTO dialog_act4 VALUES (7, "I know. I mean,  the special effects in both those movies seem really hokey now,  but I'm sure they were exciting at the time. Do you remember how cool we thought the Internet was when it first came out in the early 90s?", 3);
INSERT INTO dialog_act4 VALUES (2, "I think that even films that revolutionize the industry can still pale in how great they are,  when compared to the book they come from.", 3);
INSERT INTO dialog_act4 VALUES (6, "Did you see the new Oz movie they made with James Franco?", 2);
INSERT INTO dialog_act4 VALUES (14, "I just can't get that joke. My humor needs to be actually funny,  you know?", 4);
INSERT INTO dialog_act4 VALUES (8, "I agree. I wonder how many people had access to color screens at the time,  though. Or did that matter?", 5);
INSERT INTO dialog_act4 VALUES (0, "Big magic,  fantasy books are hard to condense. Take Lord of the Rings,  the whole world could never have fit into just a couple books. It is really its own reality.", 2);
INSERT INTO dialog_act4 VALUES (4, "And it may not have been especially innovative,  but making The Wizard of Oz a musical was a really smart choice. They could use that to communicate the emotion much better than a straightforward movie.", 3);
INSERT INTO dialog_act4 VALUES (11, "I'm pretty sure that is because Rowling used magic to condense that world down into pages,  stuff you muggles would not understand.", 4);


#Mapping commands
INSERT INTO mappings VALUES (0, 0, 0, None, None, None);
INSERT INTO mappings VALUES (1, 0, 1, 0, 0, 0);
INSERT INTO mappings VALUES (2, 0, 1, 1, None, None);
INSERT INTO mappings VALUES (3, 0, 1, 2, 1, 1);
INSERT INTO mappings VALUES (4, 0, 2, None, None, None);
INSERT INTO mappings VALUES (5, 0, 1, 2, 0, 2);
INSERT INTO mappings VALUES (6, 0, 1, None, None, None);
INSERT INTO mappings VALUES (7, 0, 3, None, None, None);
INSERT INTO mappings VALUES (8, 0, 4, None, None, None);
INSERT INTO mappings VALUES (9, 0, 5, 3, None, None);
INSERT INTO mappings VALUES (10, 0, 6, None, None, None);
INSERT INTO mappings VALUES (11, 0, 1, 2, None, None);
INSERT INTO mappings VALUES (12, 0, 1, 2, 2, None);
INSERT INTO mappings VALUES (13, 0, 1, 2, 3, 3);
INSERT INTO mappings VALUES (14, 0, 5, 4, None, None);
INSERT INTO mappings VALUES (15, 0, 5, 5, None, None);
INSERT INTO mappings VALUES (16, 0, 5, None, None, None);
INSERT INTO mappings VALUES (17, 0, 5, 6, None, None);
INSERT INTO mappings VALUES (18, 0, 1, 2, 4, None);
INSERT INTO mappings VALUES (19, 0, 1, 2, 3, 4);
INSERT INTO mappings VALUES (20, 0, 1, 2, 3, 5);
INSERT INTO mappings VALUES (21, 0, 1, 2, 3, 6);
INSERT INTO mappings VALUES (22, 0, 1, 2, 1, 7);
INSERT INTO mappings VALUES (23, 0, 7, None, None, None);
INSERT INTO mappings VALUES (24, 0, 1, 2, 1, 8);
INSERT INTO mappings VALUES (25, 0, 1, 2, 3, None);
INSERT INTO mappings VALUES (26, 0, 1, 2, 0, 9);
INSERT INTO mappings VALUES (27, 0, 1, 2, 1, 10);
INSERT INTO mappings VALUES (28, 0, 1, 2, 0, None);
INSERT INTO mappings VALUES (29, 0, 1, 2, 5, None);
INSERT INTO mappings VALUES (30, 0, 8, 7, None, None);
INSERT INTO mappings VALUES (31, 0, 8, 8, None, None);
INSERT INTO mappings VALUES (32, 0, 8, 9, None, None);
INSERT INTO mappings VALUES (33, 0, 8, 10, None, None);
INSERT INTO mappings VALUES (34, 0, 1, 2, 1, None);
INSERT INTO mappings VALUES (35, 0, 9, None, None, None);
INSERT INTO mappings VALUES (36, 0, 8, None, None, None);
INSERT INTO mappings VALUES (37, 0, 1, 11, None, None);
INSERT INTO mappings VALUES (38, 0, 10, None, None, None);
INSERT INTO mappings VALUES (39, 0, 1, 2, 6, None);
INSERT INTO mappings VALUES (40, 0, 1, 2, 7, None);
INSERT INTO mappings VALUES (41, 0, 1, 2, None, None);
INSERT INTO mappings VALUES (42, 0, 1, 2, 0, 11);
INSERT INTO mappings VALUES (43, 0, 11, None, None, None);
INSERT INTO mappings VALUES (44, 1, 12, 12, 8, 12);
INSERT INTO mappings VALUES (45, 1, 12, 13, 9, 13);
INSERT INTO mappings VALUES (46, 1, 13, None, None, None);
INSERT INTO mappings VALUES (47, 1, 12, 13, 9, None);
INSERT INTO mappings VALUES (48, 1, 12, 13, 9, 14);
