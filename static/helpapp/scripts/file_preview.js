jQuery(document).ready(function ($) {
                
    var maxFileSize = 10 * 1024 * 1024; // (байт) Максимальный размер файла (10мб)
    var queue = {};
    var form = $('form#uploadFiles');
    var imagesList = $('#uploadImagesList');
    var fileUploadWrapper = $('#fileUploadWrapper');

    var itemPreviewTemplate = imagesList.find('.item.template').clone();
    itemPreviewTemplate.removeClass('template');
    imagesList.find('.item.template').remove();
    
    
    $('#id_userFile').on('change', function () {
        $('.img-wrap').remove();
        document.getElementById("deleteLink").style.display="flex";
        document.getElementById("uploadImagesList").style.display="flex";
        document.getElementById("uploadFiles").style.height="920px";
        var files = this.files;
        var fileCount = 5;
        
        for (var i = 0; i < fileCount; i++) {
            var file = files[i];
            
            //Раскомментировать если нужно принимать только изображения
            // if ( !file.type.match(/image\/(jpeg|jpg|png|gif|pdf)/) ) {
            //     alert( 'Фотография должна быть в формате jpg, png или gif' );
            //     continue;
            // }


            if (files.length > fileCount) {
                document.getElementById("deleteLink").style.display="none";
                alert('Нелья загрузить больше 5 файлов');
                document.getElementById("uploadImagesList").style.display="none";
                
                break;
                
            }

            if ( file.size > maxFileSize ) {
                alert( 'Размер файла не должен превышать 10 Мб' );
                document.getElementById("deleteLink").style.display="none";
                continue;
            }

            preview(files[i]);
        }

        this.value = '';
    });

    // Создание превью
    function preview(file) {
        
        var reader = new FileReader();
        reader.addEventListener('load', function(event) {
            var img = document.createElement('img');
            var itemPreview = itemPreviewTemplate.clone();
            itemPreview.find('.img-wrap img').attr('src', event.target.result);
            itemPreview.data('id', file.name);

            imagesList.append(itemPreview);

            queue[file.name] = file;

        });
        reader.readAsDataURL(file);
    }

    // Удаление фотографий
    fileUploadWrapper.on('click', '.deleteLink', function () {
        var item = $(this).closest('.item'),
            id = item.data('id');

        delete queue[id];

        document.getElementById("id_userFile").value = "";
        $('.img-wrap').remove();
        //$('#userfile')[0].reset();
        document.getElementById("uploadImagesList").style.display="none";
        document.getElementById("deleteLink").style.display="none";
        document.getElementById("uploadFiles").style.height="760px";
    });

    // Отправка формы
    form.on('submit', function(event) {

        var formData = new FormData(this);

        for (var id in queue) {
            formData.append(queue[id]);
        }

        $.ajax({
            url: '../file_send.php',
            type: 'POST',
            data: formData,
            async: true,
            
            success: function(msg) {
                console.log(msg);
                if (msg == 'ok') {
                  alert('Сообщение отправлено');
                  $('#form').trigger('reset'); // очистка формы
                } else {
                  alert('Ошибка');
                  }
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
});