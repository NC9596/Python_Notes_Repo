print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/     Miscellaneous       * 
             *                                       *
             *****************************************                                           
''')

'''
        *************      Iterator      *************
    > Used for iteration, i.e. to get One value at a time
    > To get the values in a List, we can do it in three ways:
        -> using index [line 28 in Collection/Sequence]
        -> using for loop [line 100 in Statements and Loops]
        -> using Iterator
    Note: Behind the scene, ITERATOR works for the FOR LOOP, i.e. next function
    
    > To get the iterator from the list and get the values:
                    [use iter() method] [use __next__() method]
                                        [or use next(<iteratorName>) method]           
        
        <iteratorName> = iter(<listName>)
        <iteratorName>.__next__()
        
    > Iterator preserves the state of the last fetched value
        -> i.e. the value will not be repeated
    
    > We can create a new Custom Iterator as well
        -> For that we should define two important methods:
            1. __iter__(self)
            2. __next__(self)
    
    Ex: nums = [7,8,9,5]
        it = iter(nums)
        print(it.__nect__())   ==> 7
        print(it.__nect__())   ==> 8
        
        print(next(it))        ==> 9
        
    Ex: class TopTen:
            
            def __init__(self):
                self.num = 1
                
            def __iter__(self):
                return self
                
            def __next__(self):
                if self.num <= 10
                    val = self.num
                    self.num += 1
                    return val
                else:
                    raise StopIteration
                    
        values = TopTen()
        
        print(next(values))  ==> 1
        
        for i in values:     ==> 2 3 4 5 6 7 8 9 10  // 1 won't be repeated
            print(i)
'''

'''
            *************      Generators      *************
    > In Iterators, if we should create an Iterator, 
      we should define iter() and next() method in the custom Iterator class
    > Generator will give Iterators for us, we should just create a function
        BUT, instead of return keyword, we should use yield keyword
      i.e. a function with yield keyword is a Generator
    > yield will return ONE value at a time
    
    > Usecase: When we want to fetch records from a database,
                instead to fetching the whole list of records,
                we can yield one record at a time
    
    Ex: def topten():
            
            n = 1
            
            while n<=10
                yield n
                n += 1
                
        values = topten()
        print(values.__next__())   ==> 1
        print(values.__next__())   ==> 2
            
        for i in values:           ==> 3 4 5 6 7 8 9 10
            print(i)
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Exception Handling      *************
    > We have three types of errors:
        1. Compile time Error/Syntactical Error:
            --> wrong syntax, missing :, wrong spelling, etc.
            --> Easy to handle, because it is a developer side errors
        
        2. Logical Error:
            --> error in the logic of the code, i.e. wrong output
                Ex: 2+3 should be 5, but gives 4
            --> Easy to handle, because we can test the softwares
        
        3. Run time Error:
            --> error in run time,
                i.e. wrong input, divide by 0, file not found etc.
                    Ex: 6/3 = 2, But 6/0 = Error
            --> Difficult to handle, because error caused by the user side
            --> Run time error will stop the execution of the program
            --> Exception Handling is to be done to handle the error 
                so that the execution will not stop even if there is an error
                
    > Exception Handling:
        --> Put the code that may cause run time error inside a 
            try except finally block [similar to try catch finally in java]
            
            try:
                <blockOfCode>
            except <ExceptionType> as e:
                <exceptionBlockOfCode>
                print(e)    
            finally:
                <finallyBlockOfCode>
        
        --> Try block will be executed, if there is an error,
            ONLY then the except block will be executed
        --> In either of the case, finally block will be executed and 
            the execution continues
        
        Ex: | a = 5                                         |
            | b = 0                                         |
            |                                               |
            | print(a/b)    ==> Error, and execution stops  |
            |                                               |
            | print('Bye')  //Will not be executed          |
            
            a = 5
            b = 0
            
            try:
                print(a/b)                        //gets an error
            except Exception:
                print('Hey, Cannot divide by 0')  ==> Hey, Cannot divide by 0
            finally:
                print('Use this again')           ==> Use this again
           
                                                  //execution will not stop          
            print('Bye')                          ==> Bye
          
            
        --> There are lot of exceptions like ValueError, etc
            But, Exception is the general one. i.e. Exception will handle all
            
            But we can handle different exceptions specifically   
            
            Ex: a = 5
                try:
                    b = int(input('Enter a number: '))
                    print('5 /',b,'=',a/b)
                    
                except ZeroDivisionError as e:           //handles 0 division
                    print('Hey, Cannot divide by 0', e)
                
                except ValueError as e:                 //handles value error
                    print('Invalid Input')
                    
                except Exception as e:                  //handles all other errors
                    print('Something went wrong....')
                
                //If b is given as 'p' ==> Value error except block is called,etc.
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Threads      *************
    > Thread is a light weight process
    > By default, every execution has 1 thread, i.e. main thread
    > To create a thread and start the thread. 
        --> the class should extend Thread class
            [Thread class belongs to threading module ==> from threading import *]
        --> to start the thread, we should call the start() method of Thread class
            [start() method will internally call the run() method] 
            
    > There is a join() method, that will tell main thread to wait till 
                                the sub threads completes their execution
                                
    > Advantages of threads: We can use multiple cores and 
                             can execute things simultaneously
                                
    Note: sleep() method of time module, will delay the execution
    
    Ex: from time import sleep     //to delay the execution
        from threading import *
        class Hello(Thread):
            def run(self):         //name should be run()
                for i in range(2):
                    print('Hello')
                    sleep(1)       //delay of 1 second
            
        class Hi(Thread):
            def run(self):         //name should be run() 
                for i in range(2):
                    print('Hi')
                    sleep(1)       //delay of 1 second
                    
        t1 = Hello()               //thread t1 created
        t2 = Hi()                  //thread t2 created
        
        t1.start()
        sleep(0.2)    //if not given, then there is possibility of a collision
                            i.e. HelloHi
        t2.start()            
        
        //Now, we have 3 threads[main, t1, t2]
        
        t1.join() //will tell main thread to wait till t1 completes the execution
        t2.join() //will tell main thread to wait till t2 completes the execution

        print('Bye')  //Main thread will continue the execution
        
        ==> O/P :: Hello
                   Hi
                   Hello
                   Hi
                   Hello
                   Bye 
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      File Handling      *************
    > To store a data in a persistent way, we can use: 
                        1. Relational Database(for complex data)
                        2. File (for simple format, like text, etc.)
    > To open the file in a program:
        -> Use open() method:
        
            <fileObjectName> = open('<fileName>','<openPurpose>')
            
            file must be present within the project
            <openPurpose> => 'r'  : Read
      
                             'rb' : Read in Binary Mode [for image files]
            
                           | 'w'  : Write [writes in an empty file] 
        [First checks if   |
          file is present, | 'wb' : Write in Binary Mode [for image files] 
          if not present,  |
          it will create   | 'a'  : Append [will append data to existing file]
          one for us]      |
                           | 'ab'  : Append in Binary Mode [for image files]
            
            --> File provides certain important functions:
                1. read()      ==> reads the entire file
                2. readline()  ==> reads the file line by line, 
                                   it uses inbuilt pointer like Iterator
                
       NOTE: If for loop is used to read a file, it will read one line at a time
                
                3. readline(<noOfCharacters>) ==> reads the first <noOfCharacters> 
                                                  of a line 
                                                  
                4. write('<data>')  ==> Writes <data> into the file ['w' and 'a']           
                            
        Ex: f1 = open('MyData','r') //open MyData in read mode
            print(f1.readline())    //reads the 1st line
            print(f1.readline(3))   //reads the first 3 characters of line 2
            print(f1.read())        //reads the rest of the file
            
            f2 = open('ABC','w')    //open/create ABC in write mode 
            f2.write('First Line')  //writes on line 1
            
            f2 = open('ABC','a')    //open/create ABC in append mode 
            f2.write('\n')
            f2.write('Second Line') //writes on line 2
            
            //To copy MyData into ABC
            f1 = open('MyData','r') //open MyData in read mode
            f2 = open('ABC','w')    //open/create ABC in write mode
            
            for data in f1:
                f2.write(data)      //Will copy MyData into ABC
                
            //image files:
            f3 = open('python.jpg','rb') //open python image in read binary mode
            print(f3.readline())         //reads first line of the image
            
            f4 = open('python-copy.jpg','wb') //open/create python-copy.jpg 
                                                  in write binary mode
            for i in f3:
                f4.write(i)         //Will copy python.jpg into python-copy.jpg
            
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Database Connection[MySQL]      *************
    
    > Should install a connector by running the code:
        
        pip3 install mysql-connector
        
    > Then do the following:
        --> import mysql.connector
            
            # For connecting with the DB
            <dbName> = mysql.connector.connect(host='<hostName>', 
                                               user='<userName>',
                                               passwd='<passWord>')

            # Will give cursor to work with DB (it is like pointer to DB
            <cursorName> = <dbName>.cursor()
            
            # To execute ANY SQL statement, and data is stored in the cursor
            <cursorName>.execute('<SQL Query>')
            
            for i in <cursorName>:
                print(i)
                
            # We can also store data somewhere from cursor using fetchall() method
            <variableName> = <cursorNae>.fetchall()     ==> will get a tuple
            
            # We can store one data at a time using fetchone() method
            <variableName> = <cursorNae>.fetchone()     ==> will get a tuple
                
    Ex: import mysql.connector as mydb
            
        mydb = mydb.connect(host='localhost', 
                            user='root',
                            passwd='Softtek@2022')

        mycursor = mydb.cursor()

        # Cursor
        mycursor.execute('select * from java8_assignment.customer_table')

        for i in mycursor:
            print(i)              ==> (1, 'Nandish', 2)
                                      (2, 'Dharsh', 2)
                                      (3, 'Sushanth', 1)
                                      (4, 'Lokesh', 1)
                                      (5, 'Ashik', 1)
                                      (6, 'Supriya', 2)
        
        # Result - fetchAll                            
        result = mucursor.fetchall()
        
        for i in result:
            print(i)              ==> (1, 'Nandish', 2)
                                      (2, 'Dharsh', 2)
                                      (3, 'Sushanth', 1)
                                      (4, 'Lokesh', 1)
                                      (5, 'Ashik', 1)
                                      (6, 'Supriya', 2)
    
        # Result - fetchOne
        result = mucursor.fetchone()
        
        print(result)             ==> (1, 'Nandish', 2)
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Socket Programming      *************
    > Client(send request) and Server(return response)
    > The base of the network is the Socket(Client and Server)
    
    > Port:
        --> The server should have a portNumber
            [Even client will have a portNumber, will be auto created]
        --> Should choose a port number that is free(like 9999)
        
        Note: Range for port number: 0 to 65535
    
    > Type of connection:
        --> TCP [Transmission Control Protocol]
            * Connection oriented network
              [i.e. first create a connection then only we can communicate]  
                
        --> UDP [User Datagram Protocol]
            * Connection less network
              [i.e. no need to create a connection, based on the address it will 
                reach the destination]
            * Drawback: cannot check if it is sent to the destination address
    
    > To achieve socket programming:
      
      1. Server Socket ::
      
        --> import socket module
        --> create a socket: use socket() method 
        
                * By convention we use 's' for socket and 'c' for client 
                
                i.e. s = socket.socket() 
            
        --> We should bind the socket with the port number: Use bind() method
        
                i.e. s.bind(('<address>',<portNumber>))

                        <address>: localhost ==> if both server and client is
                                                 the same machine
                                                 
        --> Then, start listening for the clients:
                * also we can specify the number of clients to wait for, we should 
                  use listen() method
                  
                  i.e. s.listen(3)
                  
                * use while loop to continuously listen to the clients: accept()
                    it will return the client socket and address of the client
                    
                    i.e. while True:
                         c, addr = s.accept()
                         
        --> Receive data from client: use recv() method
            
                    i.e. c.recv(<bufferSize>)
        
        --> Then, send something to the client: use send() method
                
                i.e. c.send(bytes(<data>),<format>)
            
        --> Close the connection: use close() method
                
                i.e s.close()
            
      2. Client Socket ::
      
        --> import socket module
        
        --> create a socket: use socket() method 
        
                * By convention we use 's' for socket and 'c' for client 
                
                i.e. c = socket.socket()
                
        --> Server will bind the server to the port, hence client should just use:
                use connect() method
                
                i.e. c.connect(<data>)
                
        --> Send data to server: use send() method
                
                i.e. c.send(bytes(<data>,<format>))
                
        --> Accept the data from the server: use recv() method
                
                i.e. c.recv(<bufferSize>)
            
    Ex: Ex_server.py is the server
        Ex_client.py is the client 
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Email Sending      *************
    
    > NOT recommended, because, it is not secure
    > Steps:
        1. import smtplib module, smtp is a protocol for mailing
                                  [simple mail transfer protocol]
        
        2. create a server: use smtplib.SMTP('<serverAddress>',<portNumber>)
            different for different providers:
             'smtp.gmail.com', 587 => for gmail

        3. We should have a connection: use starttls() method
            server.starttls()
        
        4. login: use login(<userName>,<passWord>) method
        
        5. send mail: use sendmail(<senderMail>,<receicerMail>,<body>) method
    
    Ex: import smtplib
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        
        server.starttls()
        
        server.login('nc9596.test@gmail.com', 'qwert12345!@#$%')
        
        server.sendmail('nc9596.test@gmail.com','nandi9596@gmail.com','Hi')
        
        print('Mail Sent')

''' 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      What Next      *************
    > Web development: Django
    > Machine Learning: TensorFlow
    > Data Visualization/Extraction: Panda
    > For Scripting

'''