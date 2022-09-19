package projektKacperKalinowski;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class Testowanie {
    main TEST;

    @Before
    public void setUp(){
        TEST = new main();
    }

    @Test
    public void  testchckpsl(){
        assertTrue(TEST.chckPsl("99051702191"));
    }
    @Test
    public void testliczby(){
        assertTrue(TEST.liczby("99051702191"));
    }
}