from win32com.client import constants
import win32con
import win32gui
import time
import win32com.client
import pythoncom


#捕捉QQ登录窗口，2秒后隐藏和显示窗口
# while True:
#     qqWin = win32gui.FindWindow("TXGuiFoundation","QQ")
#     win32gui.ShowWindow(qqWin, win32con.SW_HIDE)
#     time.sleep(2)
#     win32gui.ShowWindow(qqWin, win32con.SW_SHOW)
#     time.sleep(2)
#语音识别，将文字转换为语音
# dehua = win32com.client.Dispatch("SAPI.SPVOICE")
# dehua.Speak("Lwt是个好同志")
class SpeechRecognition:
    def __init__(self,wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener =win32com.client.Dispatch("SAPI.SpSharedRecongnizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule",constants.SRATopLevel + constants.SRADynamic,0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.ADDWordTransition(None,word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule",1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("started successfully")
    def say(self,phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self,StreamNumber,StreamPosition,RecognitionType,Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：",newResult.PhraseInfo.GetText())

if __name__ =='__main__':
    wordsToAdd = ["关机","取消关机","记事本","画图板","写字板","设置","关闭记事本"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()