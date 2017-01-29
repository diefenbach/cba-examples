$(() => {
    $(document).on('mouseover', '.origin', function() {
        let originId = $(this).attr('id');
        originId = originId.split('-')[1];
        $('#translation-' + originId).show();
    });

    $(document).on('mouseout', '.origin', function() {
        let originId = $(this).attr('id');
        originId = originId.split('-')[1];
        $('#translation-' + originId).hide();
    });

    $('.untranslated').on('click', function() {
        const that = $(this);
        $.get('/translate', data => {
            that.html(data);
        });
    });
});
