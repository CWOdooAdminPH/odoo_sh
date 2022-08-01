odoo.define('codewerk_sale.field.html', function (require) {

    const FieldHtml = require('web_editor.field.html')

    FieldHtml.include({
        _getValue: function () {
            let value = this._super.apply(this, arguments);

            let text = $(value).text();
            // Removing spaces & html spaces
            let isNotEmpty = text && text.split('&nbsp;').join('').replace(/\s/g, '')


            return isNotEmpty ? value : '<p><br></p>';
        },
    });
});
