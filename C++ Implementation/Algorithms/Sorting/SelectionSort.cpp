void selectionSort(int arr[], int n){
    for(int i=0; i<n; i++){
        int currMinIndex = i;
        bool newMin = false;

        for(int j=i+1; j<n; j++){
            if(arr[currMinIndex] > arr[j]){
                currMinIndex = arr[j];
                newMin = true;
            }
        }

        if(newMin){
            // swap
            int temp = arr[i];
            arr[i] = arr[currMinIndex];
            arr[currMinIndex] = temp;
        }
    }
}


int main(){
    const int n = 5;
    int arr[n] = {3, 5, 1, 2, 4};
    selectionSort(arr, n);
    return 0;
}