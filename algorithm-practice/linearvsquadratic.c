#include<stdio.h>

/*
A program to find the minimum value of an array with big O notation O(n) and O(n**2)
*/

int linear(int arr[], int n){   // arr being an array and n being length of arr
  int i, smallestnumber;        // i = index of array
  smallestnumber = arr[0];
  for (i=0; i<n; i++){
    if (smallestnumber > arr[i]){
      smallestnumber = arr[i];    // find the smallest number in the array
    };
  };
  return smallestnumber;
};

int quadratic(int arr[], int n){  // n = length of array
  int i, j, smallestnumber;
  /* loop through the array twice, compare every number to eachother, save the smaller one each time
  smallestnumber */
  for (i=0; i<n; i++){
    for (j=0; j<n; j++){
      if (arr[i] > arr[j]){
        smallestnumber = arr[j];
      };
    };
  };
  return smallestnumber;
};


int main(){
  int arr[] = {8, 17, 24, 16, 5, 3};  // set test array
  int n = 6;                          // length of array
  int smallestnumber = linear(arr, n);  // run linear() and set smallestnumber as the the return
  int smallestnumberquadratic = quadratic(arr, n);  // run quadratic() and set smallestnumber as the the return
  printf("the smallest number calculated linearly is: %d \n", smallestnumber);
  printf("the smallest number calculated quadratically is: %d \n", smallestnumberquadratic);
  return 0;
};

/* Output:

>>> ./linearvsquadratic
the smallest number calculated linearly is: 3
the smallest number calculated quadratically is: 3
*/
