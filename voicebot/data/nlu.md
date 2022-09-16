## intent:greet
- Hey
- Hello
- Hi
- good morning
- good evening
- hey there

## intent:welcome
- welcome
- greetings

## intent:name
- my name is [sanjay](name)
- [parth](name:parth) this side
- It's [ashish](name)
- [ashish](name:ashish) is my name
- [Ashish](name)
- [Rahul](name)
- [ashish](name)
- [bineet](name)
- I am [vinay](name)

## intent:registration
- the registration number is [TN 75 AA 7106](registration)
- [AP-21-BP-7331](registration)
- [HR-26-TC-7174](registration)
- [ap01-DR-0117](registration)
- [ka01 SE 1011](registration)
- [gu01 LM 1011](registration)
- [JK-01-LC-1232](registration)
- [TN-75-AT-7106](registration)
- [AP-21-BP-7331](registration)
- [PU-19-DS-0343](registration)
- [MA-12-RN-1289](registration)
- [hr-26-TC-7174](registration)
- [MP 01 BI 1011](registration)
- [UP 01 HL 1011](registration)
- [AP 01 DR 1011](registration)
- [RA 01 SE 1011](registration)
- [gu01 LM 1011](registration)
- [DL01 LM 1011](registration)
- [AP01 lm1011](registration)
- [MH01 LM 1011](registration)

## regex:registration
- ^[A-Z]{2}-[0-9]{1,2}-[A-Z]{1,2}-[0-9]{3,4}$

## intent:email
- my email id is [sanjay@gmail.com](email)
- [sa127@gmail.com](email)
- [parth.sharma@gmail.com](email)
- [bineetsingh54@gmail.com](email)
- [rahulgupta123@gmail.com](email)
- [sanjay@gmail.com](email)
- [sanjayyadav@gmail.com](email)
- [parth_sharma@gmail.com](email)
- [bsingh@gmail.com](email)
- [rahulg123@gmail.com](email)
- [sanjay@gmail.com](email)
- [vinaypandey@gmail.com](email)
- [psharma@gmail.com](email)
- [bineetsingh@gmail.com](email)
- [rahulgupta123@gmail.com](email)
- [sanjay@gmail.com](email)
- [sanjayyadav@gmail.com](email)
- [parthsharma@gmail.com](email)
- [bineetsingh@gmail.com](email)
- [rahulgupta123@gmail.com](email)

## regex:email
- ^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$

## intent:phone
- my phone number is [91-889 966 7722](phone)
- [91 7233569871](phone)
- [91-8859473158](phone)
- [91 932 178 2755](phone)
- [91654 894 8484](phone)
- [917233 569871](phone)
- [91885 947 3158](phone)
- [9193217 82755](phone)
- [91654 894 8484](phone)
- [91 7233 569871](phone)
- [91885 947 3158](phone)
- [91-93217 82755](phone)
- [91654 894 8484](phone)


## regex:phone
- ^[1-9]{1}[0-9]{9}$

## intent:bye
- Bye
- Goodbye
- see you around
- see you later
- Thank you so much!
- Thanks
- tnx
- thank you so much
- thanks alot
- ty

## intent:affirm
- yes
- yeah
- yup
- indeed
- of course
- that sounds good
- correct
- it is correct
- it's correct

## intent:deny
- no
- No
- nope
- no thanks
- nope thank you
- it is not
- it's not
- thank you, no
- I don't think so
- don't like that
- no way
- not really

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?