<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Test nao projet app" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="HelloWorld" src="HelloWorld/HelloWorld.dlg" />
    </Dialogs>
    <Resources>
        <File name="vacuum1" src="behavior_1/vacuum1.ogg" />
        <File name="texte" src="texte.txt" />
        <File name="Liste mot" src="Liste mot.txt" />
        <File name="mot reconu" src="mot reconu.txt" />
        <File name="reponce" src="reponce.txt" />
        <File name="nombre" src="nombre.txt" />
        <File name="Sound" src="Sound.wav" />
        <File name="ficher1" src="teste speache phython/ficher1.mp3" />
        <File name="teste 1" src="teste speache phython/teste 1.py" />
        <File name="QuestionReponse" src="QuestionReponse.txt" />
        <File name="swiftswords_ext" src="behavior_1/swiftswords_ext.mp3" />
        <File name="reponce" src="teste speache phython/reponce.txt" />
        <File name="teste niv1" src="teste speache phython/teste niv1.py" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_frf" src="behavior_1/ExampleDialog/ExampleDialog_frf.top" topicName="ExampleDialog" language="fr_FR" />
        <Topic name="HelloWorld_frf" src="HelloWorld/HelloWorld_frf.top" topicName="HelloWorld" language="fr_FR" />
    </Topics>
    <IgnoredPaths>
        <Path src="Liste mot.txt" />
    </IgnoredPaths>
</Package>
