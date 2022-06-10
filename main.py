from tkinter import *

def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)

    if(e.get().upper()=="HI"):
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: How are you? ")
    elif(e.get().upper()=='HELLO'):
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: How are you? ")
    elif (e.get().lower() == "i'm fine and you?"):
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: Nice to hear that")
        text.insert(END, "\n" + "Bot: I'm fine too")
        text.insert(END, "\n" + "Bot: How may i help you? ")
    elif (e.get().lower() == "need to see bank balance in my account"):
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: Bank balance in the account is Rs Xxxxx.xx.")
    elif (e.get().lower() == "how should i transfer the amount to other bank accounts"):
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: Necessary steps: ")
        text.insert(END, "\n" + "Bot: 1. Log in to the Online Bank portal.")
        text.insert(END, "\n" + "Bot: 2. Click on ‘Other Bank Transfer’ under the ‘Payments/Transfer’ tab if you wish to transfer money to another bank’s account.")
        text.insert(END, "\n" + "Bot: 3. If you wish to transfer to an account within the same bank, click ‘Accounts of Others – Within Same Bank’..")
        text.insert(END, "\n" + "Bot: 4. A screen will appear according to your selection, choose the type of transaction you would like to make and click ‘Proceed’..")
        text.insert(END, "\n" + "Bot: 5. From the list, choose the account you wish to make the fund transfer from.")
        text.insert(END, "\n" + "Bot: 6. Now, enter the amount you wish to transfer and remarks if any.")
        text.insert(END, "\n" + "Bot: 7. Choose the beneficiary account to transfer the funds.")
        text.insert(END, "\n" + "Bot: 8. You can also instruct when the fund transfer must take place using the option available.")
        text.insert(END, "\n" + "Bot: 9. Agree to the terms and conditions by selecting the checkbox and click ‘Submit’.")
        text.insert(END, "\n" + "Bot: 10. The following screen will show all the details you entered for review. Once you are sure that all the details are correct, click ‘Confirm’.")
        text.insert(END, "\n" + "Bot: 11. You will receive a high-security password on the registered mobile number. Enter this password and click ‘Confirm’ to complete the authentication process.")
        text.insert(END, "\n" + "Bot: 12. A confirmation message will be displayed on the screen to mark the completion.")
    else:
        e.delete(0, END)
        text.insert(END, "\n" + "Bot: Sorry I didn't get it.")

root = Tk()
root.title('CHATBOT IN PYTHON')
root.resizable(0,0)
text = Text(root,bg='#d3d8db')
text.grid(row=0,column=0,columnspan=2)
text.insert(END, "\n" + "Bot: Hello! ")
e=Entry(root,width=80)
send=Button(root,text='Send',bg='white',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.mainloop()