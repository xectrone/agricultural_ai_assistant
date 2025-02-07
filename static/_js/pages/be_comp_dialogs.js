/*
 *  Document   : be_comp_dialogs.js
 *  Author     : pixelcave
 *  Description: Custom JS code used in Dialogs Page
 */

// SweetAlert2, for more examples you can check out https://github.com/sweetalert2/sweetalert2
class pageDialogs {
  /*
   * SweetAlert2 demo functionality
   *
   */
  static sweetAlert2() {
    // Set default properties
    let toast = Swal.mixin({
      buttonsStyling: false,
      target: '#page-container',
      customClass: {
        confirmButton: 'btn btn-primary m-1',
        cancelButton: 'btn btn-danger m-1',
        input: 'form-control'
      }
    });

    // Init a simple dialog on button click
    let swalSimple = document.querySelector('.js-swal-simple');
    
    if (swalSimple) {
      swalSimple.addEventListener('click', e => {
        toast.fire('Hi, this is just a simple message!');
      });
    }

    // Init an success dialog on button click
    let swalSuccess = document.querySelector('.js-swal-success');
    
    if (swalSuccess) {
      swalSuccess.addEventListener('click', e => {
        toast.fire('Success', 'Everything was updated perfectly!', 'success');
      });
    }

    // Init an info dialog on button click
    let swalInfo = document.querySelector('.js-swal-info');
    
    if (swalInfo) {
      swalInfo.addEventListener('click', e => {
        toast.fire('Info', 'Just an informational message!', 'info');
      });
    }

    // Init an warning dialog on button click
    let swalWarning = document.querySelector('.js-swal-warning');
    
    if (swalWarning) {
      swalWarning.addEventListener('click', e => {
        toast.fire('Warning', 'Something needs your attention!', 'warning');
      });
    }

    // Init an error dialog on button click
    let swalError = document.querySelector('.js-swal-error');
    
    if (swalError) {
      swalError.addEventListener('click', e => {
        toast.fire('Oops...', 'Something went wrong!', 'error');
      });
    }

    // Init an question dialog on button click
    let swalQuestion = document.querySelector('.js-swal-question');
    
    if (swalQuestion) {
      swalQuestion.addEventListener('click', e => {
        toast.fire('Question', 'Are you sure about that?', 'question');
      });
    }

    // Init an example confirm dialog on button click
    let swalConfirm = document.querySelector('.js-swal-confirm');
    
    if (swalConfirm) {
      swalConfirm.addEventListener('click', e => {
        toast.fire({
          title: 'Are you sure?',
          text: 'You will not be able to recover this imaginary file!',
          icon: 'warning',
          showCancelButton: true,
          customClass: {
            confirmButton: 'btn btn-danger m-1',
            cancelButton: 'btn btn-secondary m-1'
          },
          confirmButtonText: 'Yes, delete it!',
          html: false,
          preConfirm: e => {
            return new Promise(resolve => {
              setTimeout(() => {
                resolve();
              }, 50);
            });
          }
        }).then(result => {
          if (result.value) {
            toast.fire('Deleted!', 'Your imaginary file has been deleted.', 'success');
            // result.dismiss can be 'overlay', 'cancel', 'close', 'esc', 'timer'
          } else if (result.dismiss === 'cancel') {
            toast.fire('Cancelled', 'Your imaginary file is safe :)', 'error');
          }
        });
      });
    }

    // Init an example confirm alert on button click
    let swalCustom = document.querySelector('.js-swal-custom-position');
    
    if (swalCustom) {
      swalCustom.addEventListener('click', e => {
        toast.fire({
          position: 'top-end',
          title: 'Perfect!',
          text: 'Nice Position!',
          icon: 'success'
        });
      });
    }
  }

  /*
   * Init functionality
   *
   */
  static init() {
    this.sweetAlert2();
  }
}

// Initialize when page loads
Dashmix.onLoad(() => pageDialogs.init());
