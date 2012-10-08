(function(){

var manage_delSLAs = new Zenoss.Action({
    text: _t('Delete SLA') + '...',
    id: 'manage_delSLAs-item',
    permission: 'Manage DMD',
    handler: function(btn, e){
        var win = new Zenoss.dialog.CloseDialog({
            width: 300,
            title: _t('Delete SLA'),
            items: [{
                xtype: 'form',
                buttonAlign: 'left',
                monitorValid: true,
                labelAlign: 'top',
                footerStyle: 'padding-left: 0',
                border: false,
                items: [{
                    xtype: 'textfield',
                    name: 'deviceIp',
                    fieldLabel: _t('Hostname or IP'),
                    id: "slaTitleField",
                    width: 260,
                    allowBlank: false
                }, {
                    xtype: 'textfield',
                    name: 'community',
                    fieldLabel: _t('RO Community'),
                    id: "slaRoCommunityField",
                    width: 260,
                    allowBlank: false
                }, {
                    xtype: 'textfield',
                    name: 'rttIndex',
                    fieldLabel: _t('SLA Index'),
                    id: "slaIndexField",
                    width: 260,
                    allowBlank: false
                }],
                buttons: [{
                    xtype: 'DialogButton',
                    id: 'manage_delSLAs-submit',
                    text: _t('Delete'),
                    formBind: true,
                    handler: function(b) {
                        var form = b.ownerCt.ownerCt.getForm();
                        var opts = form.getFieldValues();
                        
                        Zenoss.remote.OpenStackRouter.addOpenStack(opts,
                        function(response) {
                            if (response.success) {
                                new Zenoss.dialog.SimpleMessageDialog({
                                    message: _t('Delete SLA job submitted.'),
                                    buttons: [{
                                        xtype: 'DialogButton',
                                        text: _t('OK')
                                    }, {
                                        xtype: 'button',
                                        text: _t('View Job Log'),
                                        handler: function() {
                                            window.location =
                                                '/zport/dmd/JobManager/jobs/' +
                                                response.jobId + '/viewlog';
                                        }
                                    }]
                                }).show();
                            }
                            else {
                                new Zenoss.dialog.SimpleMessageDialog({
                                    message: response.msg,
                                    buttons: [{
                                        xtype: 'DialogButton',
                                        text: _t('OK')
                                    }]
                                }).show();
                            }
                        });
                    }
                }, Zenoss.dialog.CANCEL]
            }]
        });
        win.show();
    }
});

Ext.ns('Zenoss.extensions');
Zenoss.extensions.adddevice = Zenoss.extensions.adddevice instanceof Array ?
                              Zenoss.extensions.adddevice : [];
Zenoss.extensions.adddevice.push(manage_delSLAs);

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.SLAsPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'SLAs',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'rttMonCtrlAdminOwner'},
                {name: 'rttMonCtrlAdminTag'},
                {name: 'rttMonCtrlAdminRttType'},
                {name: 'hasMonitor'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
               id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 120,
                sortable: true
            },{
                id: 'rttMonCtrlAdminOwner',
                dataIndex: 'rttMonCtrlAdminOwner',
                header: _t('Owner'),
                sortable: true,
            },{
                id: 'rttMonCtrlAdminTag',
                dataIndex: 'rttMonCtrlAdminTag',
                header: _t('Group'),
                sortable: true
            },{
                id: 'rttMonCtrlAdminRttType',
                dataIndex: 'rttMonCtrlAdminRttType',
                header: _t('Type'),
                sortable: true,
                width: 200,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 70,
                sortable: true,
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]
        });
        ZC.SLAsPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('SLAsPanel', ZC.SLAsPanel);
ZC.registerName('SLAs', _t('SLA'), _t('SLAs'));
})();
