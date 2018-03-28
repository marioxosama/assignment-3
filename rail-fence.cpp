// FCI – Programming 1 – 2018 - Assignment 2
// Program Name:  	 	rail-fence.cpp
// Last Modification Date: 2/03/2018
// Author1 and ID and Group: 	xxxxx xxxxx
// Author2 and ID and Group: 	xxxxx xxxxx
// Author3 and ID and Group: 	xxxxx xxxxx
// Teaching Assistant: 	 // Purpose:..........  	xxxxx xxxxx




#include <iostream>
#include<float.h>
#include<string>
#include<cmath>
using namespace std;


void encrypt3(string x)
{
        for(int i=0; i<x.length();i++){
            if(x[i]==' '){
            x.erase(i,1);                        //first for loop to remove spaces
            }
        }
        for(int i=0; i<x.length(); i++){         //second one starts from first letter to print letter and leave 3 then print another
            cout<<x[i];
            i+=3;

        }
        for(int i=1; i<x.length();i++){          //third loop starts from second letter to print letter and leave 1 and so on
            cout<<x[i];
            i+=1;
        }
        for(int i=2; i<x.length(); i++){         //4th loop start from 3rd letter to print one and leave 3
            cout<<x[i];
            i+=3;
        }                                        // so we get the zigzag shape

}

void decrypt3(string y)
{
    int k=0;
   string firstArray[y.length()] , secondArray[y.length()] , thirdArray[y.length()];
   for(int i=0; i<y.length(); i++){
        firstArray[i]=y[k];                      // made 3 arrays represent the 3 rows and no. of columns is word length
        i+=3; k++;
    }                                            // first loop add first char , leave 3 spaces , then add second and so on
    for(int i=1; i<y.length(); i++){
        secondArray[i]=y[k];
        i+=1; k++;                               // 2nd loop starts from index 2 , add the next char and leave one space
    }
    for(int i=2; i<y.length(); i++){
        thirdArray[i]=y[k];                      // 3rd loop starts from index 3 , add the next char and leave 3 spaces , thats how we get the zigzag shape
        i+=3; k++;
    }
    for(int i=0; i<y.length();i++){
        cout<<firstArray[i]<<secondArray[i]<<thirdArray[i];    //last loop print char vertically so we get them on the right order
    }
}


int main()
{

    string decrypted , encrypted;
    int  key , type;
    cout<<"welcome to rail-fence Encryption program"<<endl;
    cout<<"1. Encrypt"<<endl;
    cout<<"2. Decrypt"<<endl;
    cout<<"3. Exit"<<endl;
    cin>>type;


    if(type==1){
        cout<<"Enter message required to encrypt : ";
        cin.ignore();
        getline(cin,decrypted);
        encrypt3(decrypted);

    }
    else if(type==2){
        cout<<"Enter message required to decrypt : ";
        cin.ignore();
        getline(cin,encrypted);
        decrypt3(encrypted);

    }
    else if (type==3){
        return 0;
    }




}


