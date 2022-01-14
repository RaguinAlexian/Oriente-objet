class Chapitre:
    def __init__(self,goldModif,pvModif,txt,links):
        self.__modifGold = goldModif
        self.__modifPV = pvModif
        self.__ListeLiens = links
        self.__text = txt

    def getListeLiens(self):
        listeLiens = {0 : "Chapitre 0", 1 : "chapitre 1", 2 : "chapitre 2", 3 : "chapitre 3", 4 : "chapitre 4", 5 : "chapitre 5", 6 : "chapitre 6", 7 : "chapitre 7"}
        for i in range(self.__ListeLiens):
            if(i == self.__ListeLiens):
                self.__ListeLiens = listeLiens[i]
        return self.__ListeLiens

    def getPvPerdus(self, new):
        if (new > 150) :
            self.__modifPV = 150
        else : 
            self.__modifPV = self.__modifPV + new
        return self.__modifPV

    def GetOrGagne(self, change):
        self.__modifGold = self.__modifGold + change
        return self.__modifGold
    
    def getText(self):
        print(self.__text)

class Personnage:
    def __init__(self,name,gold,pv):
        self.__nom = name
        self.__monnaie = gold
        self.__vie = pv

    def getNom(self):
        return self.__nom
    def getOr(self):
        return self.__monnaie
    def getPv(self):
        return self.__vie
    def perdPv(self, modif):
        if (modif > 150) :
            self.__vie = 150
        else : 
            self.__vie = self.__vie + modif
        return self.__vie 
    def gagneOr(self, modifG):
        if (modifG <= -self.__monnaie) :
            self.__monnaie = 0
        else : 
            self.__monnaie = self.__monnaie + modifG
        return self.__vie 

Georges = Personnage("Balruf Georges", 100, 150)
Chapitre0 = Chapitre(100,0,"Vous arrivez à votre guilde pour vous inscire. Après votre inscription vous recevez 100 d'or et on vous fait comprendre que chaque quête accomplit sera taxé par la guilde, vous êtes actuellement au maximum de votre forme (150 pv). Vous décidez finalement de prendre une quête." ,0)
Chapitre1 = Chapitre(25,-35,"Vous avez donc prit la quête pour chasser des loups. Alors que vous arrivez sur place, vous êtes attaqué par des loups. Vous arrivez à les terrasser et décidez donc de récupérer la fourrure. Par chance peu après un marchand ambulant se présente à vous et vous lui vendez tout.",1)
Chapitre2 = Chapitre(0,+100,"Après cette mésaventure vous décidez de continuer dans la grotte. Alors que vous avancez, vous tombez sur une fontaine de fée. Vous la buvez et vous vous sentez comme neuf.", 2)
Chapitre3 = Chapitre(0, 0, "Vous prenez une direction au hasard et marchez avec quelques provisions. À force de marche vous arrivez face à un panneau, sur l'une des faces il est écrit 'Danger de mort' et sur l'autre 'Repaire de bandits'. Quel choix allez-vous faire ? \n1- Prendre le chemin mortel \n2- Prendre le chemin vers le repaire des bandits",3)
Chapitre4 = Chapitre(0, -200, "Alors que vous essayer de remonter cette pente, une pierre se dérobe sous votre main et vous tombez tête la première sur le sol, votre nuque fait un sacré bruit, mais au moins maintenant vous pouvez voir où vous vous grattez quand vous avez la main dans le dos",4)
Chapitre5 = Chapitre(0,-200,"Bhouahahaha bonne blague... ... Ha vraiment ? Bon eh bien alors que vous avancez dans le désert pour affronter cette salamandre géant vous vous rendez commpte qu'un pauvre couteau ne va pas suffire. C'est barbecue pour la salamandre semble-t-il.",5)
Chapitre6 = Chapitre(200,-100,"Alors que vous décidez d'aller rejoindre votre quête pour combattre de satanés bandits, vous tombez sur une calèche accompagnée de gardes. Vous vous rendez compte que ces personnes et vos bandits s'affrontent, vous plongez pour les aider. Les bandits sont plutôt nombreux, sans cette escorte vous serez très certainement mort... À l'intérieur vous pouvez voir un baron et sa femme apeurés.",6)

victoire = False
saisie = 0

while(victoire == False):
    print("Vous êtes Balruf Georges, vous venez d'atteindre vos 21 ans quand vous décidez de devenir aventurier. L'inscription n'a rien de bien compliqué et vous avez soif d'aventure bien que vous n'ayez rien pour combattre hormis un petit couteau.")
    Chapitre0.getText()
    Georges.gagneOr(100)
    print("Plusieurs choix s'offrent à vous, vous pouvez : \n1- Aller vous inscrire dans la guilde des aventuriers \n 2- Partir à l'aventure de vous-même \n 3- Vous recouchez et abandonnez ce rêve stupide")
    while(saisie > 3 or saisie == 0):   
        saisie = int(input("Veuillez saisir votre choix : 1, 2 ou 3 : "))
    if(saisie == 1) :
        saisie = 0
        Chapitre0.getText()
        Georges.gagneOr(100)
        print("Petit rappel sur votre état : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
        print("Vous voilà donc inscrit et devant le tableau des quêtes. Il y a de nombreuses quêtes, préférez-vous prendre un quête : \n1- De bas niveau \n2- De niveau moyen \n3- De haut niveau ?")
        while(saisie > 3 or saisie == 0):   
            saisie = int(input("Veuillez saisir votre choix : 1, 2 ou 3 : "))
        if(saisie == 1) :
            saisie = 0
            Chapitre1.getText()
            Georges.gagneOr(25)
            Georges.perdPv(-35)
            print("Petit rappel sur votre état : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
            print("Après votre combat contre les loups vous vous semblez affaiblit, une montagne vient vous barrez la route. Vous en faites le tour jusqu'à tomber dans un trou, vous dévalez la pente vous blessant d'avantage. À la fin de tout ceci, vous vous retrouvez face à une crevasse")
            Georges.perdPv(-10)
            print("Vous pouvez soit : \n1- Continuer dans la grotte \n2- Continuer dans la grotte")
            while(saisie > 2 or saisie == 0):   
                saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
            if(saisie == 1):
                saisie = 0
                Chapitre2.getText()
                Georges.perdPv(+100)
                print("Petit rappel sur votre état : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
                print("Merci d'avoir joué à cette démo.")
                victoire = True
            if(saisie == 2): 
                saisie = 0
                Chapitre4.getText()
                Georges.perdPv(-200)
                print("Merci d'avoir joué à cette démo.")
                victoire = True
        if(saisie == 2):
            saisie = 0
            Chapitre6.getText()
            Georges.perdPv(-100)
            Georges.gagneOr(250)
            print("Ça c'était du combat épique. Votre vaillance vous a valu d'être bien vu du noble, il vous récompense grâcement et vous invite à rejoindre son escorte jusqu'à la prochaine ville.")
            print("Merci d'avoir joué à cette démo.")
            victoire = True
        if(saisie == 3):
            saisie = 0
            Chapitre5.getText()
            Georges.perdPv(-200)
            print("Merci d'avoir joué à cette démo.")
            victoire = True
    if(saisie == 2) :
        saisie = 0
        Chapitre3.getText()
        print("Petit rappel sur votre état : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
        while(saisie > 2 or saisie == 0):   
            saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
        if(saisie == 1) :
            saisie = 0
            print("Il est vrai qu'au moyen-âge le taux de personnes illettrées était haut, mais je vous ai prévenu... Vous avancez, encore et encore, une brume vient doucement vous entourez. Puis vous disparaissez à jamais de ce monde sans que personne ne comprenne d'où")
            victoire = True
        if(saisie == 2) :
            saisie = 0
            print("Vous avancez jusqu'au repaire. Là-bas vous faites la recontre de plusieurs de ces scélérats. Le chef vient se présenter à vous avec un grand marteau, visiblement ils sont très nombreux. Il vous pose alors une question 'Que viens-tu faire par ici ?' Bonne question ça, que venez-vous faire ? \n1- Les affronter \n2- Les rejoindre")
            while(saisie > 2 or saisie == 0):   
                saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
            if(saisie == 1) :
                saisie = 0
                print("Vous lui sortez votre plus grande punchline avant de vous faire tabassez par le groupe.")
                Georges.gagneOr(-250)
                Georges.perdPv(-149)
                print("Après vous avoir dépouillé, le chef des bandits vous fait prisonnier et se sert de vous comme otage.")
                print("Petit rappel sur votre état : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
                print("Merci d'avoir joué à cette démo.")
                victoire = True
            if(saisie == 2) :
                saisie = 0
                print("Le chef des bandits se met à rire avant de vous faire passer quelques épreuves pour vérifier vos dires. Quelques jours plus tard alors que vous dépouillez un marchand itinérant, le chef vient officialiser votre appartenance à sa bande avec un tatouage.")
                print("Merci d'avoir joué à cette démo.")
                victoire = True
    if(saisie == 3) :
        saisie = 0
        print("Vous avez raison, vaut mieux se coucher et être en forme pour travailler les champs demain")
        print("Merci d'avoir joué à cette démo.")
        victoire = True

            

