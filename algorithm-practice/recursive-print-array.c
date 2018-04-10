#include <stdio.h>
/*
Program to print out the contents of an array recursively
March 28, 2018  Nate Weeks
*/

// given arr is the array to be printed, n is the size of the
// array and i is the starting index, print the contents of the array
int recursive_print(int arr[], int n, int i){
  if(i == n){
    return 0;
  }else {
    printf("%d\n", arr[i]);
    i++;
    return recursive_print(arr, n, i);
  };
};

int main(){
  int arr[] = {4, 7, 9, 6};
  recursive_print(arr, 4, 0);
  return 0;
};
