/*
 *  Document   : op_auth_two_factor.js
 *  Author     : pixelcave
 *  Description: Custom JS code used in Two Factor Page
 */

class pageAuthTwoFactor {
  /*
   * Init Two factor functionality
   *
   */
  static init2fa() {
    let num1 = document.getElementById("num1");
    let num2 = document.getElementById("num2");
    let num3 = document.getElementById("num3");
    let num4 = document.getElementById("num4");
    let num5 = document.getElementById("num5");
    let num6 = document.getElementById("num6");

    // Focus the first number input on load
    num1.focus();

    // Move focus to the next input
    num1.addEventListener("keyup", () => {
      if (this.isNumber(num1.value)) {
        num2.focus();
      } else {
        num1.value = '';
      }
    });
    
    num2.addEventListener("keyup", () => {
      if (this.isNumber(num2.value)) {
        num3.focus();
      } else {
        num2.value = '';
      }
    });
    
    num3.addEventListener("keyup", () => {
      if (this.isNumber(num3.value)) {
        num4.focus();
      } else {
        num3.value = '';
      }
    });

    num4.addEventListener("keyup", () => {
      if (this.isNumber(num4.value)) {
        num5.focus();
      } else {
        num4.value = '';
      }
    });

    num5.addEventListener("keyup", () => {
      if (this.isNumber(num5.value)) {
        num6.focus();
      } else {
        num5.value = '';
      }
    });

    num6.addEventListener("keyup", () => {
      if (this.isNumber(num6.value)) {
        document.getElementById("form-2fa").submit();
      } else {
        num6.value = '';
      }
    });
  }

  /*
   * Check if is number
   *
   */
  static isNumber(value) {
    if (['1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(value)) {
      return true;
    }

    return false;
  }

  /*
   * Init functionality
   *
   */
  static init() {
    this.init2fa();
  }
}

// Initialize when page loads
Dashmix.onLoad(() => pageAuthTwoFactor.init());
