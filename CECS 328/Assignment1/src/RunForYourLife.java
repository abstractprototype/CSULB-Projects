import java.util.Scanner;
import java.util.Random;

public class RunForYourLife {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int[]array = null;
		int choice = 0;
		long startTime;
		long endTime;
		long duration;
		double durationMilli;

		while(choice != 1) {
			System.out.println("\n1. Quit the Program");
			System.out.println("2. Time Freddy's algorithm");
			System.out.println("3. Time Susie's algorithm");
			System.out.println("4. Time Johnny's algorithm");
			System.out.println("5. Time Sally's algorithm");
			choice = input.nextInt();
		
			switch(choice) {
			case 1:
				break;
			case 2:
				array = randomArray();
				freshmen(array);
				startTime = System.nanoTime();
				freshmen(array);
				endTime = System.nanoTime();
				duration = (endTime - startTime);
				durationMilli = (double)duration/1000000;
				//displayArray(array);
				
				System.out.println("\nDuration: " + duration);
				System.out.println("\nDuration: " + durationMilli + " milliseconds");
				break;
			case 3:
				array = randomArray();
				sophomore(array);
				startTime = System.nanoTime();
				sophomore(array);
				endTime = System.nanoTime();
				duration = (endTime - startTime);
				durationMilli = (double)duration/1000000;
				//displayArray(array);
		
				System.out.println("\nDuration: " + duration);
				System.out.println("\nDuration: " + durationMilli + " milliseconds");
				break;
			case 4:
				array = randomArray();
				junior(array, 0, array.length - 1);//because array starts at 0
				startTime = System.nanoTime();
				if(array.length > 0)// prevent crashes when array size is 0
					junior(array, 0, array.length - 1);
				endTime = System.nanoTime();
				duration = (endTime - startTime);
				durationMilli = (double)duration/1000000;
				//displayArray(array);
				
				System.out.println("\nDuration: " + duration);
				System.out.println("\nDuration: " + durationMilli + " milliseconds");
				break;
			case 5:
				array = randomArray();
				senior(array);
				startTime = System.nanoTime();
				senior(array);
				endTime = System.nanoTime();
				duration = (endTime - startTime);
				durationMilli = (double)duration/1000000;
				//displayArray(array);
			
				System.out.println("\nDuration: " + duration);
				System.out.println("\nDuration: " + durationMilli + " milliseconds");
				break;
			default:
				System.out.println("Invalid Input");
			}
		}
		testMain();
	}
	
	public static int testMain() {
		int[]testArray1 = {4,-1,-5,-7,8,2,2,32,11,7};
		int[]testArray2 = {-2,1,-3,5,10,40,12,-6,-2,15,-10};
		int[]testArray3 = {};
		int[]testArray4 = {-5,-25,-10,-23,-81,-21,-12,-55,-2,-3};
		int[]testArray5 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int[]testArray6 = {10,2,42,1,29,6,5,3,4,13};
		
		System.out.println("\nFreshmen Test: ");
		System.out.println(freshmen(testArray1));
		System.out.println(freshmen(testArray2));
		System.out.println(freshmen(testArray3));
		System.out.println(freshmen(testArray4));
		System.out.println(freshmen(testArray5));
		System.out.println(freshmen(testArray6));
		
		System.out.println("\nSophomore Test: ");
		System.out.println(sophomore(testArray1));
		System.out.println(sophomore(testArray2));
		System.out.println(sophomore(testArray3));
		System.out.println(sophomore(testArray4));
		System.out.println(sophomore(testArray5));
		System.out.println(sophomore(testArray6));
		
		System.out.println("\nJunior Test: ");
		System.out.println(junior(testArray1, 0, testArray1.length-1));
		System.out.println(junior(testArray2, 0, testArray2.length-1));
		System.out.println(junior(testArray3, 0, testArray3.length-1));
		System.out.println(junior(testArray4, 0, testArray4.length-1));
		System.out.println(junior(testArray5, 0, testArray5.length-1));
		System.out.println(junior(testArray6, 0, testArray6.length-1));
		
		System.out.println("\nSenior Test: ");
		System.out.println(senior(testArray1));
		System.out.println(senior(testArray2));
		System.out.println(senior(testArray3));
		System.out.println(senior(testArray4));
		System.out.println(senior(testArray5));
		System.out.println(senior(testArray6));
		
		return 0;
	}
	
	public static int[] randomArray() {
		Scanner input = new Scanner(System.in);
		System.out.println("Please input a seed value");
		int s = input.nextInt();
		System.out.println("Please input a seed size");
		int n = input.nextInt();
		Random rand = new Random(s);
		int[]array = new int[n];
		for(int i = 0; i < n; i++) {
			array[i] = rand.nextInt(200)-100;
		}
		return array;
	}

	public static int freshmen(int[]array) {
	
		int max = 0;
		int sizeOfArray = array.length; //size of array
		for(int i = 0; i < sizeOfArray; i++) {
			for(int j = i; j < sizeOfArray; j++) {
				int thisSum = 0;
				for(int k = i; k <= j; k++) {
					thisSum = thisSum + array[k];
				}
				if(thisSum>max) {
					max = thisSum;
				}
			}
		}
		return max;
	}
	public static int sophomore(int[]array){
		int max = 0;
		int sizeOfArray=array.length;
		for(int i = 0; i < sizeOfArray; i++) {
			int thisSum = 0;
			for(int j = i; j < sizeOfArray; j++) {
				thisSum = thisSum + array[j];
				if(thisSum > max) {
					max = thisSum;
				}
			}
		}
		return max;
	}
	public static int junior(int[]array, int left, int right) {
		if(array.length == 0)
		{
			return 0;
		}
		
		if(left == right) {
			if(array[left] > 0) {
				return array[left]; //base case return the one item in the subarray if it is positive
			}
			return 0;
		}
		
		
		
		int center = ((left+right)/2);
		int maxLeftSum = junior(array, left, center);
		int maxRightSum = junior(array, center + 1, right);
		
		int maxLeftBorder = 0;
		int leftBorder = 0;
		for(int i = center; i >= left; i--) {
			leftBorder = leftBorder + array[i];
			if(leftBorder > maxLeftBorder) {
				maxLeftBorder = leftBorder;
			}
		}
		
		int maxRightBorder = 0;
		int rightBorder = 0;
		for(int i = center + 1; i <= right; i++) {
			rightBorder = rightBorder + array[i];
			if(rightBorder > maxRightBorder) {
				maxRightBorder = rightBorder;
			}
		}
		
		return MaxSum(maxLeftSum, maxRightSum, maxLeftBorder + maxRightBorder);
	}
	public static int MaxSum(int maxLeftSum, int maxRightSum, int maxLeftRight) {
		
		  if(maxLeftSum > maxRightSum && maxLeftSum > maxLeftRight)
	        {
	            return maxLeftSum;
	        }
	      else if(maxRightSum > maxLeftRight)
	        {
	        	return maxRightSum;
	        }
	      else
	        {
	        	return maxLeftRight;
	        }
	}

	public static int senior(int[]array) {
		int max = 0;
		int thisSum = 0;
		int sizeOfArray=array.length;
		for(int i = 0; i < sizeOfArray; i++) {
			thisSum = thisSum + array[i];
			if(thisSum > max) {
				max = thisSum;
			}
			else if(thisSum < 0) {
				thisSum = 0;
			}
		}
		return max;
	
	}
	
	public static void displayArray(int[]array) {
		for(int i =0; i < array.length; i++) {
			System.out.print(array[i] + " " );
		}
	}

}


