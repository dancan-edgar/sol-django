$(function (){

    let galleryUrl = $('body').find('a.gallery');

    galleryUrl.on('click', function (e){
        e.preventDefault();

        $('<div class="modal-dialog modal-dialog-centered"><div class="modal-content">\n' +
            '      <div class="modal-header">\n' +
            '        <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>\n' +
            '        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\n' +
            '      </div>\n' +
            '      <div class="modal-body">\n' +
            '        ...\n' +
            '      </div>\n' +
            '      <div class="modal-footer">\n' +
            '        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>\n' +
            '        <button type="button" class="btn btn-primary">Understood</button>\n' +
            '      </div></div>').appendTo(document.body)
    });
})
