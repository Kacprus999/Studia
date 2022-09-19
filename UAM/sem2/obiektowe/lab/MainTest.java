package com.company;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MainTest {
    Main main;

    @Before
    public void setUp(){
        main = new Main();
    }

    @Test
    public void  checkPeselTest(){
        assertTrue(main.checkPesel("0122004120"));
    }
    @Test
    public void onlyDigitsTest(){
        assertTrue(main.onlyDigits("0122004120"));
    }
}