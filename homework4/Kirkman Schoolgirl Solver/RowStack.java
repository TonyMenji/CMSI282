import java.util.Stack;

import org.junit.Assert;

public class RowStack extends Stack<Schoolgirl> {
       
        @Override
        public Schoolgirl push(Schoolgirl item) {
             
                return super.push(item);
        }

        @Override
        public synchronized Schoolgirl pop() {
                
                return super.pop();
        }


        @Override
        public synchronized String toString() {
                return super.toString();
        }
}
