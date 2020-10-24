import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.Scanner;

//Implements the Map ADT using a hash table with separate chaining.
public class EagleOne<T> {
	
	private class Entry{
		public T mKey;
		public boolean mIsNil;
	}
	
	private Entry[] mTable;
	private int mCount; //the number of elements in the set
	
	//Constructs hash table with the given size
	public EagleOne(int tableSize) {
		// TODO: you must round up tableSize to the next power of 2!!!
		int round = 1;
		while(round < tableSize)
			round *= 2;
		tableSize = round;
		 // The next line is a workaround for Java not liking us making an array
	     // of a generic type. (Node is a generic type because it has generic
	     // members.)
		mTable = (Entry[])Array.newInstance(Entry.class, tableSize);
		// mTable's entries are all null initially.
	    // mTable[i] == null ---> nothing has ever lived at index i
	    // mTable[i] != null && mTable[i].mIsNil ---> something used to be here but was removed.
		mCount = 0;
	   }
	
	// Inserts the given key and value into the table, assuming no entry with
    // an equal key is present. If such an entry is present, override the entry's
    // value.
	public void add(T key) {
		// Every object in Java has a .hashCode() function that computes a h(k)
        // value for that object. Use that function for your hash table index
        // calculations. Note that in Java, .hashCode() can be negative!!! --> use absolute value.
		
		//check duplicates
		if(find(key)) {
			return;
		}
		
		if(loadFactor() > 0.8) {
			EagleOne tempo = new EagleOne(mTable.length * 2);
			for(int k = 0; k < mTable.length; k++) {
				if(mTable[k] != null) // check each index if its null i.e 2 5 6 null 6 9 null
					tempo.add(mTable[k].mKey); // adds to new array of * 2
			}
			this.mTable = tempo.mTable;
			//this.mCount = tempo.mCount;
		}
		//actually adds to each index the key and makes NIL false bc someone lives here
		int index; 
		for(int i = 0; i < mTable.length; i++) {
			index = (int)((Math.abs(key.hashCode()+ (Math.pow(i, 2) + i)/2)) % mTable.length);//probing function
			if(mTable[index] == null) {
				mTable[index] = new Entry(); //adds new index at Entry
				mTable[index].mKey = key; //add key
				mTable[index].mIsNil = false;
				mCount++;
				break;
			}
		}
	}
	
	// Returns true if the given key is present in the set.
	public boolean find(T key) {
		// Use the hash code and probing function to keep looking for this key until:
        // 1. you find a null element
        // 2. you find the key
        // 3. you fail n times.
		
		int index;
		for(int i = 0; i < mTable.length; i++) {
			index = (int)((Math.abs(key.hashCode()+ (Math.pow(i, 2) + i)/2)) % mTable.length);
			if(mTable[index] == null) {//if empty then nothing happens return false
				return false;
			}
			if(mTable[index].mKey.hashCode() == key.hashCode()) {//compares hashcode to see if you found key
				return true;
			}
		}
		return false;//returns if you can't find it
	}
	
	// Removes the given key from the set.
	public void remove(T key) {
		// Use the hash code and probing function to keep looking for this key until:
	    // 1. you find a null element
	    // 2. you find the key
	    // 3. you fail m times.
		
		int index;
		for(int i = 0; i < mTable.length; i++) {
			index = (int)((Math.abs(key.hashCode()+ (Math.pow(i, 2) + i)/2)) % mTable.length);
			if(mTable[index] == null) { //if empty then nothing happens return false
				return;
			}
			if(mTable[index].mKey.hashCode() == key.hashCode()) { //key is found so set NIL to true
				mTable[index].mIsNil = true;
				mCount--;
				return;
			}
		}
		return;
	}

	public int count() {
		return mCount;
	}

	public double loadFactor() {
		double loadFactor =  mCount / mTable.length;
		return loadFactor;
	}
	
	// scan speech, seperate into one word, remove nonalphanumeric characters, add modified word to hashset
	public static void main(String[] args) {
		EagleOne hashset = new EagleOne(50);
		File file = new File("trump_speech.txt");
	
		if(!file.exists()) {
			System.out.println("No file found");
		}else {
			try {
				Scanner scan = new Scanner(file);
				while(scan.hasNext()) {
					String token = scan.next();
					String word = token.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
					if(word.matches(".*\\w.*"))
						hashset.add(word);
					
				}
//				int count = 0;
//				 for(int i = 0; i < hashset.mTable.length; i++) {
//	                    System.out.print(i + " " + hashset.mTable[i]);
//	                    if(hashset.mTable[i] != null) {
//	                        System.out.println(" " + hashset.mTable[i].mKey);
//	                        count++;
//	                    }
//	                    else
//	                        System.out.print("\n");
//	                }
//
//	            System.out.println(hashset.count() + " " + count);
				System.out.println(hashset.count());
			}
			catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				System.out.println("File not found");
			}
		}
	}
}
