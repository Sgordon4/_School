package edu.iastate.cs472.proj2;

import edu.iastate.cs472.proj2.datatypes.Clause;
import edu.iastate.cs472.proj2.datatypes.ConjunctiveNormalForm;
import edu.iastate.cs472.proj2.datatypes.Node;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Sean Gordon
 */
public class Main {
    public static void main(String[] args) {

        ConjunctiveNormalForm KB = new ConjunctiveNormalForm();
        ConjunctiveNormalForm toProve = new ConjunctiveNormalForm();


        String pathname = "C:\\Users\\Sean\\Downloads\\sampleData.txt";

        readFileIntoKB(pathname, KB, toProve);


        //-------------------------------------------------------------------------------------------------------------
        // Begin resolving clauses and printing things

        StringBuilder output = new StringBuilder();

        output.append("\nknowledge base in clauses:\n");
        output.append(KB.printStructure()).append("\n");



        for(int i = 0; i < toProve.list.size(); i++){
            ConjunctiveNormalForm clonedKB = KB.clone();        //Make a duplicate KB so we don't overwrite anything
            Clause goalClause = toProve.list.get(i);            //Grab the next goal clause


            output.append("****************\n");
            output.append("Goal sentence ").append(i+1).append(":\n\n");
            output.append(goalClause).append("\n");
            output.append("****************\n");
            output.append("\n");


            Clause negGoalClause = goalClause.clone();//Negate goal clause
            negGoalClause.list.get(0).negated = !negGoalClause.list.get(0).negated;


            output.append("Negated goal in clauses:\n\n");
            output.append(negGoalClause).append("\n\n");

            output.append("Proof by refutation:\n\n");
            if(Resolver.proveClauseWithKB(clonedKB, negGoalClause, output))
                output.append("The KB entails ").append(goalClause).append("\n\n\n");
            else{
                output.append("No new clauses are added.\n");
                output.append("The KB does not entail ").append(goalClause).append("\n\n\n");
            }

        }

        //Print the entire output string
        System.out.println(output);
    }

    /**
     * Given a sentence string (e.g. "( Rain && Outside ) => Wet"), parses it into tokens and, using
     * edu.iastate.cs472.proj2.ExpressionToPostfix.infixToPostfix and edu.iastate.cs472.proj2.PostfixToTree.buildExpTree, builds an expression tree.
     * The expression tree is then sent to edu.iastate.cs472.proj2.TreeToCNF.recursiveCNFConvert to convert to CNF.
     *
     * @param str Sentence string to parse and convert to CNF
     * @return CNF version of str
     */
    public static ConjunctiveNormalForm stringToCNF(String str){
        String pattern = "(\\()|(\\))|(<=>)|(=>)|(\\|\\|)|(&&)|(~)|(\\w+)";
        Matcher m2 = Pattern.compile(pattern).matcher(str); //Match all individual parts

        List<String> allMatches = new ArrayList<String>();
        while (m2.find()) {
            allMatches.add(m2.group());
        }

        //Build an expression tree from the parsed operators and operands
        List<String> postfix = ExpressionToPostfix.infixToPostfix(allMatches);
        Node expressionTree = PostfixToTree.buildExpTree(postfix);

        //Convert the expression tree into CNF
        ConjunctiveNormalForm cnf = TreeToCNF.recursiveCNFConvert(expressionTree);


        //Printing these variables for testing can be done as so:
        //expressionTree.printPretty();
        //System.out.println(cnf);
        //System.out.println(cnf.printStructure());

        return cnf;
    }


    /**
     * Intakes a file conforming to the specifications in section 1 of the proj2F20-1.pdf packaged with this project.
     * The contents of the file are split up line by line and sentences are sent to edu.iastate.cs472.proj2.Resolver.stringToCNF for parsing.
     *
     * @param filepath  Location of the file to read
     * @param KB        List that will hold the clauses that make up the knowledge base
     * @param toProve   List that will contain the clauses to prove using the KB
     * @return boolean True if success, False if error
     */
    public static boolean readFileIntoKB(String filepath, ConjunctiveNormalForm KB, ConjunctiveNormalForm toProve){
        File file = new File(filepath);

        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String st;

            //Get to the knowledge base in case there are blank lines at the top of the file --------------------------
            while ((st = br.readLine()) != null){
                if(st.equals("Knowledge Base:")) break;
            }
            br.readLine();  //Skip the blank line



            //Parse through the knowledge base ------------------------------------------------------------------------
            StringBuilder sentence = new StringBuilder();
            while ((st = br.readLine()) != null){
                if(st.equals("Prove the following sentences by refutation:")) break;

                //If we haven't hit an empty line yet, this is a multi-line sentence
                else if(!st.equals("")) {
                    sentence.append(st);
                }

                //If we have hit an empty line...
                else{
                    //Parse the current string into a sentence in CNF and add it to the knowledge base
                    ConjunctiveNormalForm cnf = stringToCNF(sentence.toString());
                    KB.list.addAll(cnf.list);

                    //Set the current sentence to nothing
                    sentence = new StringBuilder();
                }
            }
            br.readLine();  //Skip the blank line



            //Parse through the sentences to prove --------------------------------------------------------------------
            sentence = new StringBuilder();
            while ((st = br.readLine()) != null){
                //If we haven't hit an empty line yet, this is a multi-line sentence
                if(!st.equals("")) {
                    sentence.append(st);
                }

                //If we have hit an empty line...
                else{
                    //Parse the current string into a sentence in CNF and add it to the toProve base
                    ConjunctiveNormalForm cnf = stringToCNF(sentence.toString());
                    toProve.list.addAll(cnf.list);

                    //Set the current sentence to nothing
                    sentence = new StringBuilder();
                }
            }

            //Because we stop when br.readline() == null, we miss the last sentence to prove. I'm too lazy to work out
            // the logic to get around that, so I'm just slapping a duplicate parsing section here:

            //Parse the final string into a sentence in CNF and add it to the toProve base
            ConjunctiveNormalForm cnf = stringToCNF(sentence.toString());
            toProve.list.addAll(cnf.list);


        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

}
