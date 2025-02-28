package edu.iastate.cs228.hw02;

/**
A class of bags whose entries are stored in a chain of linked nodes.
	The bag is never full.
@author Frank M. Carrano
@author Timothy M. Henry
@author Sean Gordon
@version 4.1
 */
public final class LinkedBag<T> implements BagInterface<T>
{
	private Node firstNode;       // Reference to first node
	private int numberOfEntries;

	public LinkedBag()
	{
		firstNode = null;
		numberOfEntries = 0;
	} // end default constructor

	/** Sees whether this bag is empty.
	    @return  True if this bag is empty, or false if not. */
	public boolean isEmpty() 
	{
		return numberOfEntries == 0;
	} // end isEmpty

	/** Gets the number of entries currently in this bag.
	    @return  The integer number of entries currently in this bag. */
	public int getCurrentSize() 
	{
		return numberOfEntries;
	} // end getCurrentSize

	/** Adds a new entry to this bag.
	    @param newEntry  The object to be added as a new entry
	    @return  True if the addition is successful, or false if not. */
	public boolean add(T newEntry)  	      // OutOfMemoryError possible
	{
		// Add to beginning of chain:
		Node newNode = new Node(newEntry);
		newNode.next = firstNode; // Make new node reference rest of chain
		// (firstNode is null if chain is empty)        
		firstNode = newNode;      // New node is at beginning of chain
		numberOfEntries++;

		return true;
	} // end add

	/** Retrieves all entries that are in this bag.
	    @return  A newly allocated array of all the entries in this bag. */
	public Object[] toArray()
	{
		// The cast is safe because the new array contains null entries
		@SuppressWarnings("unchecked")
		T[] result = (T[])new Object[numberOfEntries]; // Unchecked cast

		int index = 0;
		Node currentNode = firstNode;
		while ((index < numberOfEntries) && (currentNode != null))
		{
			result[index] = currentNode.data;
			index++;
			currentNode = currentNode.next;
		} // end while

		return result;
	} // end toArray

	/** Counts the number of times a given entry appears in this bag.
		 @param anEntry  The entry to be counted.
		 @return  The number of times anEntry appears in this bag. */
	public int getFrequencyOf(T anEntry) 
	{
		int frequency = 0;

		int counter = 0;
		Node currentNode = firstNode;
		while ((counter < numberOfEntries) && (currentNode != null))
		{
			if (anEntry.equals(currentNode.data))
			{
				frequency++;
			} // end if

			counter++;
			currentNode = currentNode.next;
		} // end while

		return frequency;
	} // end getFrequencyOf

	/** Tests whether this bag contains a given entry.
		 @param anEntry  The entry to locate.
		 @return  True if the bag contains anEntry, or false otherwise. */
	public boolean contains(T anEntry)
	{
		boolean found = false;
		Node currentNode = firstNode;

		while (!found && (currentNode != null))
		{
			if (anEntry.equals(currentNode.data))
				found = true;
			else
				currentNode = currentNode.next;
		} // end while	

		return found;
	} // end contains

	// Locates a given entry within this bag.
	// Returns a reference to the node containing the entry, if located,
	// or null otherwise.
	private Node getReferenceTo(T anEntry)
	{
		boolean found = false;
		Node currentNode = firstNode;

		while (!found && (currentNode != null))
		{
			if (anEntry.equals(currentNode.data))
				found = true;
			else
				currentNode = currentNode.next;
		} // end while

		return currentNode;
	} // end getReferenceTo

	/** Removes all entries from this bag. */
	public void clear() 
	{
		while (!isEmpty()) 
			remove();
	} // end clear

	/** Removes one unspecified entry from this bag, if possible.
    @return  Either the removed entry, if the removal
             was successful, or null. */
	public T remove()
	{
		T result = null;
		if (firstNode != null)
		{
			result = firstNode.data; 
			firstNode = firstNode.next; // Remove first node from chain
			numberOfEntries--;
		} // end if

		return result;
	} // end remove

	/** Removes one occurrence of a given entry from this bag, if possible.
    @param anEntry  The entry to be removed.
    @return  True if the removal was successful, or false otherwise. */
	public boolean remove(T anEntry) 
	{
		boolean result = false;
		Node nodeN = getReferenceTo(anEntry);

		if (nodeN != null)
		{
			nodeN.data = firstNode.data; // Replace located entry with entry in first node

			firstNode = firstNode.next;  // Remove first node
			numberOfEntries--;

			result = true;
		} // end if

		return result;
	} // end remove

	private class Node 
	{
		private T    data; // Entry in bag
		private Node next; // Link to next node

		private Node(T dataPortion)
		{
			this(dataPortion, null);	
		} // end constructor

		private Node(T dataPortion, Node nextNode)
		{
			data = dataPortion;
			next = nextNode;	
		} // end constructor
	} // end Node



	/*------------------------------------------------------------------*\
	\*------------------------------------------------------------------*/



	/** Creates a new bag that combines the contents of this bag and anotherBag.
    @param anotherBag  The bag that is to be added.
    @return  A combined bag. */
	public BagInterface<T> union(BagInterface<T> anotherBag){
		BagInterface<T> union = new LinkedBag<T>();
		Node node = this.firstNode;
		
		for(int i = 0; i < this.getCurrentSize(); i++) {
			union.add(node.data);
			node = node.next;
		}
		
		LinkedBag<T> bag = (LinkedBag<T>)anotherBag;
		node = bag.firstNode;
		for(int i = 0; i < anotherBag.getCurrentSize(); i++) {
			union.add(node.data);
			node = node.next;
		}

		return union;
	}

	/** Creates a new bag that contains those objects that occur
    in both this bag and anotherBag.
	    @param anotherBag  The bag that is to be compared.
	    @return  A combined bag. */
	public BagInterface<T> intersection(BagInterface<T> anotherBag){
		BagInterface<T> intersection = new LinkedBag<T>();
		Node node = this.firstNode;

		int frequency;
		for(int i = 0; i < this.getCurrentSize(); i++) {
			if(!intersection.contains(node.data)) {	//Checks if the item has already been added to our new bag
				
				//Finds the overlap in the specific item
				frequency = Math.min(this.getFrequencyOf(node.data), anotherBag.getFrequencyOf(node.data));	
				for(int a = 0; a < frequency; a++) {
					intersection.add(node.data);
				}
			}
			node = node.next;
		}
		return intersection;
	}

	/** Creates a new bag of objects that would be left in this bag
    after removing those that also occur in anotherBag.
	    @param anotherBag  The bag that is to be removed.
	    @return  A combined bag. */
	public BagInterface<T> difference(BagInterface<T> anotherBag){
		BagInterface<T> difference = new LinkedBag<T>();
		Node node = this.firstNode;

		int frequency;
		for(int i = 0; i < this.getCurrentSize(); i++) {
			if(!difference.contains(node.data)) {	//Checks if the item has already been added to our new bag
				
				//Finds the number of this specific item that don't match up between bags
				frequency = Math.abs(this.getFrequencyOf(node.data) - anotherBag.getFrequencyOf(node.data));	
				for(int a = 0; a < frequency; a++) {
					difference.add(node.data);
				}
			}
			node = node.next;
		}
		return difference;
	}

	/**
	  Replaces an unspecified entry in this bag with a given object.
	  @param replacement The given object
	  @return The original entry in the bag that was replaced or null if bag was empty.
	 */
	public T replace(T replacement) {
		if(this.getCurrentSize() != 0) {
			T replaced = this.firstNode.data;
			this.firstNode.data = replacement;
			return replaced;
		}
		return null;
	}

	/**
	  Removes every occurrence of a given entry from this bag.
	  @param anEntry The entry to be removed.
	 */
	public void removeEvery(T anEntry) {
		int frequency = this.getFrequencyOf(anEntry);
		for(int i = 0; i < frequency; i++) {
			remove(anEntry);
			//If need to fill, replace this with the item at end of bag
		}
	}
	
	
	public boolean equals(BagInterface<T> anotherBag) {
		if(anotherBag != null && (this.getCurrentSize() == anotherBag.getCurrentSize())) {
			if(this.difference(anotherBag) == null)
				return true;
		}
		return false;
	}
	
} // end LinkedBag



