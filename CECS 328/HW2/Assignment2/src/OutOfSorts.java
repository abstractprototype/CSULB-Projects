import java.util.Scanner;
import java.util.Random;

public class OutOfSorts {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int original[] = new int[100000];
		
		Random rand = new Random();
		int choice = 0;
		long startTime;
		long endTime;
		long duration;
		double durationMilli;
		
		warmUp();
		
		while(choice != 4) {
		System.out.println("Select a sort for the arrays: ");
		System.out.println("1. sorted ");
		System.out.println("2. random ");
		System.out.println("3. reverse ");
		System.out.println("4. Quit ");
		choice = input.nextInt();
		
		switch(choice) {
		case 1:
			for(int i = 0; i < original.length; i++) {
				original[i] = i + 1; 
			}
			break;
		case 2:
			for(int i = 0; i < original.length; i++) {
				original[i] = rand.nextInt(100000 - 1) + 1;
			}
			break;
		case 3:
			for(int i = 0; i < original.length; i++) {
				original[i] = 1000000 - i;
			}
		case 4:
			break;
		default:
			System.out.println("Invalid Input");
		}
		//printArray(original);
		int insertDuplicate[] = original.clone();
		int quickDuplicate[] = original.clone();
		
		startTime = System.nanoTime();
		insertionSort(insertDuplicate, 0, insertDuplicate.length);

		endTime = System.nanoTime();
		duration = (endTime - startTime);
		durationMilli = (double)duration/1000000;
		if(isOrdered(insertDuplicate)) {
			System.out.println("\nDuration of insert sort: " + durationMilli + " milliseconds");
		}
		
		startTime = System.nanoTime();
		quickSort(quickDuplicate, 0, quickDuplicate.length - 1);

		endTime = System.nanoTime();
		duration = (endTime - startTime);
		durationMilli = (double)duration/1000000;
		if(isOrdered(quickDuplicate)) {	
			System.out.println("\nDuration of quick sort: " + durationMilli + " milliseconds");
			System.out.println("");
		}
		}
	}

	public static boolean isOrdered(int[] clone) {
		for(int i = 0; i < clone.length - 1; i++) {
			if(clone[i] > clone[i+1]) {
				return false;
			}
		}
		return true;
	}
	
	
	public static void insertionSort(int[] insertDuplicate, int x, int n) {
		for(int i = x + 1; i < n; i++) {//start at 2nd element 0,1 so that it can check the left side
			int j, temp = insertDuplicate[i];
			for(j = i - 1; j >= 0; j--) {// overall moves to the right while checking left at the same time
				if(insertDuplicate[j] > temp) {
					insertDuplicate[j + 1] = insertDuplicate[j];
				}
				else
					break;
			}
			insertDuplicate[j+1] = temp;
			//System.out.println(insertDuplicate[i]);
		}
	}
	
	public static void quickSort(int[] quickDuplicate, int left, int right) {
		if(left < right) {
			int size = right - left + 1;
			if(size <= 10) // C is a constant chosen, we use C = 10
			{
				insertionSort(quickDuplicate,left, right + 1);
				return;
			}
			int m = findPivot(quickDuplicate, left, right, size/2);
			int j = partition(quickDuplicate, left, right, m);
			quickSort(quickDuplicate, left, j - 1);//j-1 because we dont touch the pivot
			quickSort(quickDuplicate, j + 1, right);//j+1 because we dont touch pivot
		}
	}
	
	private static int findPivot(int[] original, int left, int right, int mid) {
		int a = original[left];
		int b = original[left + mid];
		int c = original[right];
		
		if((a < b && b < c) || (c < b && b < a))
			return left + mid;
		else if((b < a && a < c) || (c < a && a < b))
			return left;
		else
			return right;
	}
	
	public static int partition(int[]original, int left, int right, int pivotIndex) {
		int pivotValue = original[pivotIndex];
		//swap(original[pivotIndex], original[right]);
		int temp = original[pivotIndex];
		original[pivotIndex] = original[right];
		original[right] = temp;
		
		int store = left;
		for(int i = left; i < right; i++) {
			if(original[i] <= pivotValue) {
				temp = original[store];
				original[store] = original[i];
				original[i] = temp;
				store++;
			}
		}
		//swap(original[right], original[store]);
		temp = original[right];
		original[right] = original[store];
		original[store] = temp;
		return store;
	}
	
	public static void printArray(int original[]) {
		for(int i = 0; i < original.length; i++) {
			System.out.println(original[i]);
		}
		System.out.println("\n");
	}
	
	public static void warmUp() {
	int[]testArray1 = {4,-1,-5,-7,8,2,2,32,11,7};
	int[]testArray2 = {-2,1,-3,5,10,40,12,-6,-2,15,-10};
	
	for(int i = 0; i < 10; i++) {
		insertionSort(testArray1, 0, testArray1.length - 1);
		insertionSort(testArray1, 0, testArray1.length - 1);
		quickSort(testArray2, 0, testArray2.length - 1);
		quickSort(testArray2, 0, testArray2.length - 1);
	}
	System.out.println("Warmup Complete!\n");
	}

}
