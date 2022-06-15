#include <iostream>
#include <vector>
#include <string>
using namespace std;

void parse(string&, vector<int>&, vector<string>&, string&, string&);

int main(){
  vector<int> vec;
  vector<string> oper;
  string str;
  getline(cin, str);
  string del1("+");
  string del2("-");

  parse(str, vec, oper, del1, del2);

  int sum = vec[0];
  for(int i = 0; i < oper.size(); i++){
    if(oper[i] == "+"){
      sum += vec[i+1];
    }else{
      sum -= vec[i+1];
      while(i+1 < oper.size() && oper[i+1] == "+"){
        sum -=  vec[i+2];
        i++;
      }
    }
  }
  cout << sum << '\n';
}

void parse(string& str, vector<int>& vec, vector<string>& oper, string& del1, string& del2){
  int pos = 0;
  string token;
  while(true){
    if(str.find(del1) == string::npos && str.find(del2) == string::npos){
      break;
    }else{
      if(str.find(del1) == string::npos){
        pos = str.find(del2);
        oper.push_back(del2);
      }else if(str.find(del2) == string::npos){
        pos = str.find(del1);
        oper.push_back(del1);
      }else{
        if(str.find(del1) < str.find(del2)){
          pos = str.find(del1);
          oper.push_back(del1);
        }else{
          pos = str.find(del2);
          oper.push_back(del2);
        }
      }

      token = str.substr(0, pos);
      vec.push_back(stoi(token));
      str.erase(0, pos+del1.length());
    }
  }
  vec.push_back(stoi(str));
}