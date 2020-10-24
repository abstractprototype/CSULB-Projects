import java.util.*;

public class WeightedGraph {

   class WeightedNode {
      int mIndex;
      private List<WeightedEdge> mNeighbors = new ArrayList<WeightedEdge>();
      
      WeightedNode(int index) {
         mIndex = index;
      }
   }

   private class WeightedEdge implements Comparable {

      private WeightedNode mFirst, mSecond;
      private double mWeight;

      WeightedEdge(WeightedNode first, WeightedNode second, double weight) {
         mFirst = first;
         mSecond = second;
         mWeight = weight;
      }

      @Override
      public int compareTo(Object o) {
         WeightedEdge e = (WeightedEdge) o;
         return Double.compare(mWeight, e.mWeight);
      }
   }

   private List<WeightedNode> mVertices = new ArrayList<WeightedNode>();

   public WeightedGraph(int numberOfVertices) {
      for (int i = 0; i < numberOfVertices; i++) {
         mVertices.add(new WeightedNode(i));
      }
   }

   public void addEdge(int firstVertex, int secondVertex, double weight) {
      WeightedNode first = mVertices.get(firstVertex);
      WeightedNode second = mVertices.get(secondVertex);
      
      WeightedEdge edge = new WeightedEdge(first, second, weight);
      first.mNeighbors.add(edge);
      second.mNeighbors.add(edge);
   }

   /**
    * Prints the graph to the console. Each vertex is printed on its own line,
    * starting with the vertex's number (its index in the mVertices list), then
    * a colon, then a sequence of pairs for each edge incident to the vertex.
    * For each edge, print the number of the vertex at the opposite end of the
    * edge, as well as the edge's weight.
    *
    * Example: in a graph with three vertices (0, 1, and 2), with edges from 0
    * to 1 of weight 10, and from 0 to 2 of weight 20, printGraph() should print
    *
    * Vertex 0: (1, 10), (2, 20) Vertex 1: (0, 10) Vertex 2: (0, 20)
    */
   public void printGraph() {

   }

   /**
    * Applies Prim's algorithm to build and return a minimum spanning tree for
    * the graph. Start by constructing a new WeightedGraph with the same number
    * of vertices as this graph. Then apply Prim's algorithm. Each time an edge
    * is selected by Prim's, add an equivalent edge to the other graph. When
    * complete, return the new graph, which is the minimum spanning tree.
    *
    * @return an UnweightedGraph representing this graph's minimum spanning
    * tree.
    */
   public WeightedGraph getMinimumSpanningTree() {
      // TODO: build and return the MST.
      return null;
   }

   /**
    * Applies Dijkstra's algorithm to compute the shortest paths from a source
    * vertex to all other vertices in the graph. Returns an array of path
    * lengths; each value in the array gives the length of the shortest path
    * from the source vertex to the corresponding vertex in the array.
    */
   public double[] getShortestPathsFrom(int source) {
      // TODO: apply Dijkstra's algorithm and return the distances array.
      
      // This queue is used to select the vertex with the smallest "d" value
      // so far.
      // Each time a "d" value is changed by the algorithm, the corresponding
      // DijkstraDistance object needs to be removed and then re-added to
      // the queue so its position updates.
      PriorityQueue<DijkstraDistance> vertexQueue = 
       new PriorityQueue<DijkstraDistance>();
      
      // Initialization: set the distance of the source node to 0, and all
      // others to infinity. Add all distances to the vertex queue.
      DijkstraDistance[] distances = new DijkstraDistance[mVertices.size()];
      distances[source] = new DijkstraDistance(source, 0);
      for (int i = 0; i < distances.length; i++) {
         if (i != source)
            distances[i] = new DijkstraDistance(i, Integer.MAX_VALUE);
         
         vertexQueue.add(distances[i]);
      }
      
      while (vertexQueue.size() > 0) {
         // Finish the algorithm.
         
         
         
         
         
         
      }
      
      
      return null;
   }

   class DijkstraDistance implements Comparable {

      int mVertex;
      double mCurrentDistance;

      DijkstraDistance(int vertex, double distance) {
         mVertex = vertex;
         mCurrentDistance = distance;
      }

      @Override
      public int compareTo(Object other) {
         DijkstraDistance d = (DijkstraDistance) other;
         return Double.compare(mCurrentDistance, d.mCurrentDistance);
      }
   }
   
   public static void main(String[] args) {
      // Use this main to test your code by hand before implementing the program.
      WeightedGraph g = new WeightedGraph(6);
      g.addEdge(0, 1, 1);
      g.addEdge(0, 2, 3);
      g.addEdge(1, 2, 1);
      g.addEdge(1, 3, 1);
      g.addEdge(1, 4, 4);
      g.addEdge(2, 3, 1);
      g.addEdge(2, 5, 2);
      g.addEdge(3, 4, 1);
      g.addEdge(3, 5, 3);
      g.addEdge(4, 5, 2);
      g.printGraph();
      
      
      double[] distances = g.getShortestPathsFrom(0);
      for (int i = 0; i < distances.length; i++) {
         System.out.println("Distance from 0 to " + i + ": " + 
          distances[i]);
         
      }
      
      WeightedGraph mst = g.getMinimumSpanningTree();
      System.out.println("Minimum spanning tree:");
      mst.printGraph();
   }
}


