void bubbleSort(int arr[], int n){
    for(int i=0; i<n; i++){
        bool swap = false;

        for(int j=0; j<n-i-1; j++){
            if(arr[j] > arr[j+1]){
                // swap
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

                swap = true;
            }
        }

        if(!swap){
            break;
        }
    }
}

int main(){
    int n = 5;
    int arr[5] = {5, 1, 4, 2, 8};
    bubbleSort(arr, n);
    return 0;
}