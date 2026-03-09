import edu.princeton.cs.algs4.Digraph;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class AnaliseGrafos {

    public static void main(String[] args) throws IOException {

        String filename = "amazon0302.txt";

        BufferedReader br = new BufferedReader(new FileReader(filename));
        String line;

        int V = 262111;
        Digraph G = new Digraph(V);

        while ((line = br.readLine()) != null) {

            if (line.startsWith("#")) continue;

            String[] parts = line.trim().split("\\s+");

            if (parts.length == 2) {

                int v = Integer.parseInt(parts[0]);
                int w = Integer.parseInt(parts[1]);

                G.addEdge(v, w);
            }
        }

        br.close();

        System.out.println("Vertices: " + G.V());
        System.out.println("Edges: " + G.E());

        double avgOutDegree = (double) G.E() / G.V();
        double maxEdges = (double) G.V() * (G.V() - 1);
        double density = G.E() / maxEdges;

        System.out.println("Average out-degree: " + avgOutDegree);
        System.out.println("Density: " + density);

        int maxIn = 0;
        int maxOut = 0;

        for (int v = 0; v < G.V(); v++) {

            int in = G.indegree(v);
            int out = G.outdegree(v);

            if (in > maxIn) maxIn = in;
            if (out > maxOut) maxOut = out;
        }

        int[] freqIn = new int[maxIn + 1];
        int[] freqOut = new int[maxOut + 1];

        for (int v = 0; v < G.V(); v++) {

            int in = G.indegree(v);
            int out = G.outdegree(v);

            freqIn[in]++;
            freqOut[out]++;
        }

        PrintWriter writerIn = new PrintWriter("distribuicao_indegree.csv");
        writerIn.println("Grau,Frequencia");

        for (int k = 0; k < freqIn.length; k++) {
            writerIn.println(k + "," + freqIn[k]);
        }

        writerIn.close();

        PrintWriter writerOut = new PrintWriter("distribuicao_outdegree.csv");
        writerOut.println("Grau,Frequencia");

        for (int k = 0; k < freqOut.length; k++) {
            writerOut.println(k + "," + freqOut[k]);
        }

        writerOut.close();

        System.out.println("\nArquivos CSV gerados:");
        System.out.println("distribuicao_indegree.csv");
        System.out.println("distribuicao_outdegree.csv");
        System.out.println("Max out-degree = " + maxOut);
        System.out.println("Max in-degree = " + maxIn);
    }
}