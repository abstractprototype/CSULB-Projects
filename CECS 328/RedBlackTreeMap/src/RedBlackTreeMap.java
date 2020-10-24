import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

// A Map ADT structure using a red-black tree, where keys must implement
// Comparable.
// The key type of a map must be Comparable. Values can be any type.
public class RedBlackTreeMap<TKey extends Comparable<TKey>, TValue> {
	// A Node class.
	private class Node {
		private TKey mKey;
		private TValue mValue;
		private Node mParent;
		private Node mLeft;
		private Node mRight;
		private boolean mIsRed;

		// Constructs a new node with NIL children.
		public Node(TKey key, TValue data, boolean isRed) {
			mKey = key;
			mValue = data;
			mIsRed = isRed;

			mLeft = NIL_NODE;
			mRight = NIL_NODE;
		}

		@Override
		public String toString() {
			return mKey + " : " + mValue + " (" + (mIsRed ? "red)" : "black)");
		}
	}

	private Node mRoot;
	private int mCount;

	// Rather than create a "blank" black Node for each NIL, we use one shared
	// node for all NIL leaves.
	private final Node NIL_NODE = new Node(null, null, false);

	//////////////////// I give you these utility functions for free.

	// Get the # of keys in the tree.
	public int getCount() {
		return mCount;
	}

	// Finds the value associated with the given key.
	public TValue find(TKey key) {
		Node n = bstFind(key, mRoot); // find the Node containing the key if any
		if (n == null || n == NIL_NODE)
			throw new RuntimeException("Key not found");
		return n.mValue;
	}
	
	

	/////////////////// You must finish the rest of these methods.

	// Inserts a key/value pair into the tree, updating the red/black balance
	// of nodes as necessary. Starts with a normal BST insert, then adjusts.
	public void add(TKey key, TValue data) {
		Node n = new Node(key, data, true); // nodes start red

		// normal BST insert; n will be placed into its initial position.
		// returns false if an existing node was updated (no rebalancing needed)
		boolean insertedNew = bstInsert(n, mRoot);
		if (!insertedNew)
			return;

		// check cases 1-5 for balance violations.
		checkBalance(n);
	}

	// Applies rules 1-5 to check the balance of a tree with newly inserted
	// node n.
	private void checkBalance(Node n) {
		if (n == mRoot) {
			// case 1: new node is root.
			n.mIsRed = false;
			return;
		}
		if(!n.mParent.mIsRed) { // case 2: P is black
			return;
		}
		// case 3: Parent and Uncle are both red 
		Node gTemp = getGrandparent(n);
		if(getUncle(n).mIsRed) { // if uncle and parent is red
			getGrandparent(n).mIsRed = true;
			getUncle(n).mIsRed = false;
			n.mParent.mIsRed = false;
			checkBalance(getGrandparent(n)); //recursively call grandpa to fix this
			return;
		}
		// new node will be either LL/RR or LR/RL
		if(n.mParent == getGrandparent(n).mLeft) {
			//n is in left subtree
			//if n is right child we need to do case 4 then case 5
			//Case 4: LR/RL
			if(n == n.mParent.mRight) {
				//rotates the parent and will be the left child of n
				singleRotateLeft(n.mParent);
				n = gTemp.mLeft.mLeft;
			}// Case 5: using LL imbalance
			singleRotateRight(gTemp);
			// parent is red and left child of n
			//color the grandparent red and parent black so no imbalance of black nodes
			n.mParent.mIsRed = false;
			gTemp.mIsRed = true;
		}
		else {//n is in right subtree
			if(n == n.mParent.mLeft) {
				singleRotateRight(n.mParent);
				n = gTemp.mRight.mRight;
			}
			singleRotateLeft(gTemp);
			n.mParent.mIsRed = false;
			gTemp.mIsRed = true;
		}

	}

	// Returns true if the given key is in the tree.
	public boolean containsKey(TKey key) {
		// TODO: using at most three lines of code, finish this method.
		// HINT: write the bstFind method first.
		return bstFind(key, mRoot).mKey.equals(key);
	}

	// Prints a pre-order traversal of the tree's nodes, printing the key, value,
	// and color of each node.
	public void printStructure() {
		// TODO: a pre-order traversal. Will need recursion.
		printStructure(mRoot);
	}
	
	//print helper
	private void printStructure(Node n) {
		if(n != NIL_NODE) {
			System.out.println(n);
			printStructure(n.mLeft);
			printStructure(n.mRight);
		}
	}

	// Returns the Node containing the given key. Recursive.
	private Node bstFind(TKey key, Node currentNode) {
		// TODO: write this method. Given a key to find and a node to start at,
		// proceed left/right from the current node until finding a node whose
		// key is equal to the given key.
		if(currentNode == null) {
			return null;
		}
		int compare = key.compareTo(currentNode.mKey);
		if(compare == 0)
			return currentNode;
		if(compare < 0)
			return bstFind(key, currentNode.mLeft);
		return bstFind(key, currentNode.mRight);
		
	}

	//////////////// These functions are needed for insertion cases.

	// Gets the grandparent of n.
	private Node getGrandparent(Node n) {
		// TODO: return the grandparent of n
		if(n.mParent == null) {
			return null;
		}
		return n.mParent.mParent;
	}

	// Gets the uncle (parent's sibling) of n.
	private Node getUncle(Node n) {
		// TODO: return the uncle of n
		if(n == null) {
			return null;
		}
		if(n.mParent == getGrandparent(n).mRight && getGrandparent(n).mRight != null) {
			return getGrandparent(n).mLeft; //if the parent is the right child of grandpa AND its NOT null then return left child of grandpa
		}
		if(n.mParent == getGrandparent(n).mLeft && getGrandparent(n).mLeft != null) {
			return getGrandparent(n).mRight;//if the parent is the left child of grandpa AND its NOT null then return right child of grandpa
		}
				
		return null;
		
	}

	// Rotate the tree right at the given node.
	private void singleRotateRight(Node n) {
		Node l = n.mLeft, lr = l.mRight, p = n.mParent;
		n.mLeft = lr;
		lr.mParent = n;
		l.mRight = n;
		n.mParent = l;

		if (p == null) { // n is root
			mRoot = l;
		}
		else if (p.mLeft == n) {
			p.mLeft = l;
		} 
		else {
			p.mRight = l;
		}
		
		l.mParent = p;
	}

	// Rotate the tree left at the given node.
	private void singleRotateLeft(Node n) {
		// TODO: do a single left rotation (AVL tree calls this a "rr" rotation)
		// at n.
		Node r = n.mRight, rl = r.mLeft, p = n.mParent;
		n.mRight = rl;
		rl.mParent = n;
		r.mLeft = n;
		n.mParent = r;

		if (p == null) { // n is root
			mRoot = r;
		}
		else if (p.mRight == n) {
			p.mRight = r;
		} 
		else {
			p.mLeft = r;
		}
		
		r.mParent = p;
	}
	


	// This method is used by insert. It is complete.
	// Inserts the key/value into the BST, and returns true if the key wasn't
	// previously in the tree.
	private boolean bstInsert(Node newNode, Node currentNode) {
		if (mRoot == null) {
			// case 1
			mRoot = newNode;
			mCount++;
			return true;
		} 
		else {
			int compare = currentNode.mKey.compareTo(newNode.mKey);
			if (compare < 0) {
				// newNode is larger; go right.
				if (currentNode.mRight != NIL_NODE) {
					
					return bstInsert(newNode, currentNode.mRight);
					
				}
				else {
					currentNode.mRight = newNode;
					newNode.mParent = currentNode;
					mCount++;
					return true;
				}
			} 
			else if (compare > 0) {
				if (currentNode.mLeft != NIL_NODE) {
					return bstInsert(newNode, currentNode.mLeft);
				}
				else {
					currentNode.mLeft = newNode;
					newNode.mParent = currentNode;
					mCount++;
					return true;
				}
			} 
			else {
				// found a node with the given key; update value.
				currentNode.mValue = newNode.mValue;
				return false; // did NOT insert a new node.
			}
		}
	}
	
	public static void main(String[] args) {
		RedBlackTreeMap<String, Integer> redblack = new RedBlackTreeMap<String, Integer>();
		File file = new File("players_homeruns.csv");
		
		if(!file.exists()) {
			System.out.println("No file found");
		}else {
			try {
				Scanner scan = new Scanner(file);
				System.out.println("First Test:");
				for(int i = 0; i < 5; i++) {
					String line = scan.nextLine();
					String[] str = line.split(",");
					redblack.add(str[0], Integer.parseInt(str[1]));
				}
				redblack.printStructure();
				
				System.out.println("\nSecond Test:");
				for(int i = 0; i < 5; i++) {
					String line = scan.nextLine();
					String[] str = line.split(",");
					redblack.add(str[0], Integer.parseInt(str[1]));
				}
				redblack.printStructure();
				
				System.out.println("\nFinding keys before entire tree:");
				System.out.println("Stan Musial: " + redblack.find("Stan Musial"));// find a leaf with two NIL children
				System.out.println("Honus Wagner: " + redblack.find("Honus Wagner"));// find a root
				System.out.println("Rogers Hornsby: " + redblack.find("Rogers Hornsby"));// find key that has one NIL child and one non-NIL child
				System.out.println("Ted Williams: " + redblack.find("Ted Williams")); // find a key that is a red node
				
				//add rest of lines of file to tree
				System.out.println("\nFinal Test: ");
				while(scan.hasNext()) {
					String line = scan.nextLine();
					String[] str = line.split(",");
					redblack.add(str[0], Integer.parseInt(str[1]));
					}
				redblack.printStructure();
				}
			
			catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				System.out.println("File not found");
			}
		
		}//Find keys again after adding rest of the tree
		System.out.println("\nFinding keys after tree:");
		System.out.println("Stan Musial: " + redblack.find("Stan Musial"));// find a leaf with two NIL children
		System.out.println("Honus Wagner: " + redblack.find("Honus Wagner"));// find a root
		System.out.println("Rogers Hornsby: " + redblack.find("Rogers Hornsby"));// find key that has one NIL child and one non-NIL child
		System.out.println("Ted Williams: " + redblack.find("Ted Williams")); // find a key that is a red node
	}
	
}

