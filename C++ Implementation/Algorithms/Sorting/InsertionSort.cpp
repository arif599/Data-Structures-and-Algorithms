void insertionSort(int arr[], int n){
    for(int i=0; i<n; i++){
        bool swap = false;

        for(int j=i-1; j>=0; j--){
            // j+1 = current element
            // j = previous element
            if(arr[j+1] < arr[j]){
                // swap
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swap = true;
            }

            if(!swap){
                break;
            }
        }
    }
}

int main(){
    int n = 5;
    int arr[5] = {5, 1, 4, 2, 8};
    insertionSort(arr, n);
    return 0;    
}