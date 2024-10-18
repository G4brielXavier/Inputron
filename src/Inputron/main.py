from time import sleep
from os import system

# INPUTRON II
# It's a Library that help in control and manage of Inputs and Outputs Terminals

class Inputron:

    # function that manage message in terminal
    def Message(self, msg:str, title:str = "", space:bool = False, iserror:bool = False, alert:bool = True, separate:str = "-"):
        
        """Create better outputs messages, alerts with this function. 
        
        Arguments:
            msg {String} Set your message here
            title {String} The Message Title [Optional]
            space {Boolean} If has space or not [Optional] default=False
            iserror {Boolean} If the message is to sinalize a error or not [Optional] default=False
            alert {Boolean} If True, add a Warn or Error after of title [Optional] default=True
            separate {String} It's the separator among title and msg [Optional] default="-"
        """
        
        if space:
            print()

        if not title == "":
            if alert:
                print(f'{title} Warn {separate} {msg}') if iserror is False else print(f'{title} Error {separate} {msg}')
            else:
                print(f'{title} {separate} {msg}') if iserror is False else print(f'{title} {separate} {msg}')
        else:
            print(f'Warn {separate} {msg}') if iserror is False else print(f'Error {separate} {msg}')

        if space:
            print()

    # function that show visual loading
    def Loading(self, msg: str = "Loading", msgComplete: str = "Complete", speed: float = 0.1, repeatTimes: int = 10, icon: list = ["...", "°..", ".°.", "..°"]):
        
        """Create a loader in format of terminal, manage and the Icon
        
        Arguments:
            msg {String} Set here your text to show while is loading [Optional] default="LOADING"
            msgComplete {String} It is message that will be shown [Optional] default="COMPLETE"
            speed {Float} It is interval in each rotated [Optional] default=0.1
            repeatTime {Integer} It is amount of time that the icon spins [Optional] default=10
            icon {List} It is the icon strings, change to other if you want [Optional] default=["|", "/", "-", "\\"]
        """
        
        bars = icon
        
        for _ in range(repeatTimes):
            for i in range(len(bars)): 
                sleep(speed)   
                system('cls')    
                print(f'{bars[i]} > {msg}')
        
        sleep(speed)
        system('cls')
        print(msgComplete)
                
    # function that control asks in terminal
    def Ask(self, ask:str, space:bool = True, isInt:bool = False, isFloat:bool = False, spaceleft:bool = True, beforesignal:str = ">", aftersignal:str = ":"):
        
        """Use this function to ask some information of user

        Arguments:
            ask {String} It is your ask 
            space {Boolean} If your asks will have spaces on top of below [Optional] default=True
            isInt {Boolean} If you want that be returned in Integer format [Optional] default=False
            isFloat {Boolean} if you want that be returned in Floating format [Optional] default=False
            spaceleft {Boolean} if you want that have a space in left side of ask [Optional] default=False
            beforesignal {String} It's the signal before of ask [Optional] default=False
            aftersignal {String} It's the signal after of ask [Optional] default=False

        """
        
        templateInput = None
        
        try:
        
            if space is True:
                print()

            if spaceleft:
                templateInput = f'    {beforesignal}{ask}{aftersignal} '
            else:
                templateInput = f'{beforesignal}{ask}{aftersignal} '
            
            askInp = input(templateInput)
            
            if not askInp == '':
                if isInt is True:
                    return int(askInp)
                
                if isFloat is True:
                    return float(askInp)
                
                if space is True:
                    print()
                    
                return askInp
            
            self.Message('It is empty, not accepted', 'Inputron', iserror=True)
            return None
            
        except Exception as err:
            inputron.Message(err, 'Nogra', True, True)
            
    # function to options Y|N
    def YN(self, ask:str, title:str = 'Question', space:bool = True):
        
        """Use this function to obtain two answer, Yes or No, you can change the options.

        Arguments:
            ask {String} It is your question.
            title {String} It is the title of question [Optional] default="Question"
            space {Boolean} If your asks will have spaces on top or below [Optional] default=True

        Raises:
            ValueError: If the answer not obtained Yes or No.

        Returns:
            Boolean: True to Yes and False to No 
        """
        
        
        if space:
            print()
            

        print(f'{title} - {ask}')
        question = input(f'[Y]es or [N]o : ')

        if question.lower() == "y":
            return True
        elif question.lower() == "n":
            return False 
        else:
            raise ValueError('Answernot Recognized')
        
        
        
        if space:
            print()
       
    # function to do a ask and choice a custom option
    def QuestionOption(self, ask:str, title:str = 'Question', space:bool = True, options=["Option 1", "Option 2", "Option 3", "Option 4"]):
        
        """Use this function to do questions and when you had various options

        Arguments:
            ask {String} It is your question.
            title {String} It is the title of question [Optional] default="Question"
            space {Boolean} If your asks will have spaces on top or below [Optional] default=True
            options {List} It's your options [Optional] default=["Option 1", "Option 2", "Option 3", "Option 4"]

        Returns:
            String: It's return the option chosen 
        """
        
        
        if space:
            print()
            

        print(f'{title} - {ask}')
        for i, v in enumerate(options):
            print(f'| {i} : {v}')
            
        print()
        option = self.Ask("Choice a option[id]", space=False, isInt=True)
        
        return options[option]
        
        
        if space:
            print()
    
    def Meet(self):
        self.Loading("Loading Inputron <test>", "Complete Inputron <test>", speed=0.2, repeatTimes=4)
        self.Message("Ola Tudo bem", "Dotket", True, alert=False, separate=">>")
        name = self.Ask("What's your name?", spaceleft=True, beforesignal="~ ", aftersignal=" >")
        self.Message(f'Welcome to Inputron, {name}!', "Dotket", alert=False, separate="-")
        self.YN("Do you like the Inputron?", "Dotket")
        language = self.QuestionOption("What's your favorite language?", "Dotket", options=["JavaScript", "Python", "Ruby", "Java"])
        self.Message(f'Your favorite language is {language}', 'Dotket', alert=False)
     
    # function to calc Average  
    def AVG(self, content:list, binsCalc:int = 4, isInt:bool = False, isFloat:bool = True, isStr:bool = False):
        
        """Use this function to calc Average of numbers to Grade

        Arguments:
            content {List} This is the list of numbers that will be used to calc
            binsCalc {Integer} It is the divider of calc [Optional] default=4
            isInt {Boolean} If the return is in integer format [Optional] default=False
            isFloat {Boolean} If the return is in floating format [Optional] default=True
            isStr {Boolean} If the return is in string format [Optional] default=False 
            
        """
        
        
        try:
            totalContents = sum(content)
            average = totalContents / binsCalc
            
            if isInt:
                return int(average)
            
            if isFloat:
                if isStr:
                    return f'{float(average):.1f}'
                return float(average)
            
            if isStr:
                return str(average) 
                 
        except Exception as err:
            self.Message(f'.~. {err}', 'Inputron', iserror=True)