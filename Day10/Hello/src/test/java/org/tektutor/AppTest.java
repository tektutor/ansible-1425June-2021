package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
	private String expectedOutput, actualOutput;

	@Test
	public void testSayHello() {
		App app = new App();

		expectedOutput = "Hello Jenkins!";
		actualOutput   = app.sayHello();

		assertEquals ( expectedOutput, actualOutput );
	}

}
