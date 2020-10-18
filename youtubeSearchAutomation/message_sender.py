from twilio.rest import Client 
 
account_sid = 'AC3d08d58df499b3e8bb28b7638cc3eece' 
auth_token = 'af730bc3df4dc3b759f586d5d207fdb1' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                            #   from_='whatsapp:+14155238886',
                              from_='whatsapp:+14076806814',
                              body='Kevin Montero is sending messages using python!',      
                              to='whatsapp:+18292670835' 
                          ) 
 
print(message.sid)

# import os 
# os.system("run.docx")
# print("Document opened!")