#!/usr/bin/python

import nltk
from nltk.corpus import wordnet as wn

class MatchingVoiceCommand :
                def __init__(self,sentence):
                                self.sentence = sentence;
                                self.commandMap = {'roll' : 0 , 'next' : 0 , 'previous' : 0 , 'buy' : 0 , 'zoom' : 0 , 'scroll' : 1 , 'find' : 1 , 'search' : 1 , 'nextImage' : 0, 'previousImage' : 0};
                                self.NounKeys = ('NN', 'NNP' , 'NNPS', 'NNS');
                                self.VerbKeys = ('VB', 'VBD' , 'VBG' , 'VBN' , 'VBP' 'VBZ');
                def tokenize(self):
                                self.tokens = nltk.word_tokenize(self.sentence);
                                self.tagged = nltk.pos_tag(self.tokens);
                def findMatchingCommand(self):
                                self.tokenize();
                                probableCommands = [];
                                lookForAnotherNoun=0;
                                argument="";
                                command='roll';
                                
                                for eachTuple in self.tagged :
                                                 
                                                if(eachTuple[1] in self.NounKeys) :
                                                                probableCommands.append(eachTuple[0].lower());

                                print probableCommands;
                                isCommandFound=False;
                                for eachProbableC  in probableCommands :
                                                indexForArg = 0;
                                                for eachProbable in self.getSynonym(eachProbableC,'v'):
                                                        if( eachProbable.lower() in self.commandMap.keys()) :
                                                                        print "I am in the key and I am"+eachProbable;
                                                                        command = eachProbable;
                                                                        lookForAnotherNoun = self.commandMap[command];
                                                                        indexForArg = probableCommands.index(eachProbableC);
                                                                        #probableCommands.remove(eachProbable);
                                                                        isCommandFound=True;
                                                                        break;
                                                if(isCommandFound):
                                                        break;                                                                

                                
                                if (lookForAnotherNoun==1) :
                                                argument = probableCommands[2:];
                               
                                return [command,(' '.join(argument))]

                def getSynonym(self,word,type):
                        print word
                        print type

                        try:
                                syn1 = wn.synset(str(word)+'.'+str(type)+'.1');
                                return syn1.lemma_names;
                        except:
                                return [];