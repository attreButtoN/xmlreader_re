from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")
    xmlfile = models.FileField(upload_to="documents/%Y/m/%d")


class Sro(models.Model):
    sro_id = models.BigIntegerField(blank=True, null=True)
    sro_name = models.CharField(max_length=512, blank=True, verbose_name="SroName")
    sro_registry_number = models.CharField(
        max_length=30, blank=True, verbose_name="SroRegistryNumber"
    )
    ogrn = models.CharField(max_length=13, null=True, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, null=True, blank=True, verbose_name="INN")
    legal_address = models.CharField(
        max_length=1024, blank=True, verbose_name="LegalAddress"
    )
    name = models.TextField(null=True, blank=True, verbose_name="Name")

    address = models.TextField(blank=True, null=True, verbose_name="Address")


class AdditionalInfo(models.Model):
    nil = models.BooleanField(null=True, blank=True, verbose_name="nil")

    def __bool__(self):
        return self.nil


class AnnullmentMessage(models.Model):
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    id_annulment = models.IntegerField(
        null=True, blank=True, verbose_name="ID_Annulment"
    )
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    is_hide = models.BooleanField(null=True, blank=True, verbose_name="IsHide")

    def __str__(self):
        return f"{self.event_time} {self.trade_id} {self.id_annulment} {self.reason}{self.is_hide}"


class Application(models.Model):
    time_begin = models.DateTimeField(null=True, blank=True, verbose_name="TimeBegin")
    time_end = models.DateTimeField(null=True, blank=True, verbose_name="TimeEnd")
    cause_of_refuse = models.TextField(
        null=True, blank=True, verbose_name="CauseOfRefuse"
    )
    rules = models.TextField(null=True, blank=True, verbose_name="Rules")

    def __str__(self):
        return f"{self.time_begin} {self.cause_of_refuse} {self.rules}"


class ApplicationData(models.Model):
    result = models.TextField(null=True, blank=True, verbose_name="Result")
    cause_of_refuse = models.TextField(
        null=True, blank=True, verbose_name="CauseOfRefuse"
    )

    def __str__(self):
        return self.result, self.cause_of_refuse


class ArbitrManager(models.Model):
    inn = models.TextField(max_length=12, null=True, blank=True, verbose_name="INN")
    sro = models.ForeignKey(Sro, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="FirstName"
    )
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="LastName"
    )
    sro_name = models.TextField(blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    reg_num = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="RegNum"
    )
    ogrn = models.CharField(max_length=15, blank=True, null=True, verbose_name="OGRNIP")
    snils = models.CharField(max_length=11, blank=True, null=True, verbose_name="SNILS")
    correspodence_address = models.CharField(
        max_length=300, blank=True, null=True, verbose_name="CorrespodenceAddress"
    )
    fio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.inn} {self.sro} {self.first_name} {self.last_name} {self.middle_name}{self.reg_num}"


class Attach(models.Model):
    # id = models.IntegerField(primary_key=True)
    file_name = models.TextField(null=True, blank=True, verbose_name="FileName")
    type = models.TextField(null=True, blank=True, verbose_name="Type")
    blob = models.TextField(null=True, blank=True, verbose_name="Blob")

    def __str__(self):
        return f"{self.file_name} {self.type} {self.blob}"


class BankruptcyCreditorCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")

    def __str__(self):
        return f"{self.full_name} {self.short_name}"


class BankruptcyCreditorPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class BiddingStateLotInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")

    def __str__(self):
        return f"{self.lot_number} {self.reason}"


class BuyerCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAddress")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")


class BuyerPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.TextField(null=True, blank=True, verbose_name="OGRNIP")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name} {self.inn} {self.ogrnip} {self.address} {self.phone} {self.email}"


class Classification(models.Model):
    idclass = models.TextField(null=True, verbose_name="IDClass")

    def __int__(self):
        return self.idclass


class CloseForm(models.Model):
    time_result = models.DateTimeField(null=True, blank=True, verbose_name="TimeResult")

    def __str__(self):
        return self.time_result


class CompanyBankrCommis(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")

    def __str__(self):
        return f"{self.full_name} {self.short_name}{self.inn}{self.ogrn}"


# class ContractNumber(models.Model):
#     nil = models.TextField(null=True)
#
#     def __bool__(self):
#         return self.nil


class ContractParticipant(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name="Name")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    is_winner = models.BooleanField(null=True, blank=True, verbose_name="IsWinner")
    is_buyer = models.BooleanField(null=True, blank=True, verbose_name="IsBuyer")

    def __str__(self):
        return f"{self.name} {self.ogrn} {self.inn} {self.is_winner} {self.is_buyer}"


class CreditorLotNumber(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")

    def __int__(self):
        return self.lot_number


class DatePublishSmi(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __bool__(self):
        return self.nil


class DebtorCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")

    def __str__(self):
        return f"{self.full_name} {self.short_name} {self.inn}{self.ogrn}"


class DeptorPerson(models.Model):
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")

    def __str__(self):
        return f"{self.inn} {self.snils} {self.first_name}{self.last_name}{self.middle_name}"


class Information(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nil


class LegalCase(models.Model):
    case_number = models.TextField(null=True, blank=True, verbose_name="CaseNumber")
    court_name = models.TextField(null=True, blank=True, verbose_name="CourtName")
    base = models.TextField(null=True, blank=True, verbose_name="Base")

    def __str__(self):
        return f"{self.case_number} {self.court_name} {self.base}"


class LotInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")

    def __int__(self):
        return self.lot_number


class OpenForm(models.Model):
    time_begin = models.DateTimeField(null=True, blank=True, verbose_name="TimeBegin")
    time_end = models.DateTimeField(null=True, blank=True, verbose_name="TimeEnd")

    def __str__(self):
        return f"{self.time_begin}{self.time_end}"


class ParticipantCompany(models.Model):
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    name = models.TextField(null=True, blank=True, verbose_name="Name")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAddress")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    full_name = models.TextField(null=True, blank=True, verbose_name="Phone")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    price_offer = models.FloatField(blank=True, null=True, verbose_name="PriceOffer")

    def __str__(self):
        return (
            f"{self.legal_address} {self.post_address} {self.phone} {self.email} {self.full_name}"
            f" {self.short_name} "
            f"{self.inn} {self.ogrn} "
        )


class ParticipantPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.IntegerField(null=True, blank=True, verbose_name="OGRNIP")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    price_info = models.FloatField(null=True, blank=True, verbose_name="PriceInfo")


class PriceInfo(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    new_price = models.FloatField(null=True, blank=True, verbose_name="NewPrice")

    def __str__(self):
        return self.lot_number, self.new_price


class StepPrice(models.Model):
    nil = models.BooleanField(null=True, blank=True)

    def __bool__(self):
        return self.nil


class TradeOrganizerCompany(models.Model):
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="ORGN")
    is_asv = models.BooleanField(null=True, blank=True, verbose_name="IsAsv")

    def __str__(self):
        return f"{self.full_name} {self.short_name} {self.inn} {self.inn} {self.ogrn} {self.is_asv}"


class TradeOrganizerPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FistName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name} {self.inn} {self.snils}"


class WinnerCompany(models.Model):
    legal_address = models.TextField(null=True, blank=True, verbose_name="LegalAddress")
    post_address = models.TextField(null=True, blank=True, verbose_name="PostAdress")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    full_name = models.TextField(null=True, blank=True, verbose_name="FullName")
    short_name = models.TextField(null=True, blank=True, verbose_name="ShortName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrn = models.TextField(null=True, blank=True, verbose_name="OGRN")

    def __str__(self):
        return f"{self.legal_address} {self.post_address} {self.phone} {self.email} {self.full_name} {self.short_name} {self.inn} {self.ogrn}"


class WinnerPerson(models.Model):
    first_name = models.TextField(null=True, blank=True, verbose_name="FirstName")
    last_name = models.TextField(null=True, blank=True, verbose_name="LastName")
    middle_name = models.TextField(null=True, blank=True, verbose_name="MiddleName")
    inn = models.TextField(null=True, blank=True, verbose_name="INN")
    ogrnip = models.TextField(null=True, blank=True, verbose_name="OGRNIP")
    snils = models.TextField(null=True, blank=True, verbose_name="SNILS")
    address = models.TextField(null=True, blank=True, verbose_name="Address")
    phone = models.TextField(null=True, blank=True, verbose_name="Phone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}{self.middle_name}{self.inn} {self.ogrnip} {self.snils} {self.address} {self.phone} {self.email}"


class ApplicationList(models.Model):
    applications_data = models.ForeignKey(
        ApplicationData, null=True, verbose_name="ApplicationData", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.applications_data


class BiddingProcessInfo(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    price_info = models.ForeignKey(
        PriceInfo, on_delete=models.CASCADE, null=True, verbose_name="PriceInfo"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.price_info}"


class ContractInfo(models.Model):
    contract_number = models.TextField(
        null=True,
        blank=True,
        verbose_name="ContractNumber",
    )
    nil = models.BooleanField(null=True, blank=True, verbose_name="nil")
    date_contract = models.DateField(
        null=True, blank=True, verbose_name="DateContract"
    )
    price = models.FloatField(null=True, blank=True, verbose_name="Price")

    def __str__(self):
        return f"{self.contract_number} {self.nil} {self.date_contract} {self.price}"


class ContractParticipantList(models.Model):
    contract_participant = models.ForeignKey(
        ContractParticipant,
        on_delete=models.CASCADE,
        verbose_name="ContractParticipant",
        null=True,
    )

    def __str__(self):
        return self.contract_participant


class CreditorLotNumberList(models.Model):
    creditor_lot_number = models.ForeignKey(
        CreditorLotNumber, on_delete=models.CASCADE, null=True, verbose_name="CreditorLotNumber"
    )

    def __str__(self):
        return self.creditor_lot_number


class Debtor(models.Model):
    debtor_company = models.ForeignKey(
        DebtorCompany, on_delete=models.CASCADE, null=True, verbose_name="DebtorCompany"
    )
    debtor_person = models.ForeignKey(
        DeptorPerson, on_delete=models.CASCADE, null=True, verbose_name="DebtorPerson"
    )

    def __str__(self):
        return f"{self.debtor_company}{self.debtor_person}"


class FailureTradeResult(models.Model):
    substantiation = models.TextField(
        null=True, blank=True, verbose_name="Substantiation"
    )
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    buyer_company = models.ForeignKey(
        BuyerCompany, on_delete=models.CASCADE, null=True, verbose_name="BuyerCompany"
    )
    buyer_person = models.ForeignKey(
        BuyerPerson, on_delete=models.CASCADE, null=True, verbose_name="BuyerPerson"
    )

    def __str__(self):
        return f"{self.substantiation} {self.price} {self.buyer_company} {self.buyer_person}"


class Lot(models.Model):
    lot_number = models.IntegerField(null=True, blank=True, verbose_name="LotNumber")
    start_price = models.FloatField(null=True, blank=True, verbose_name="StartPrice")
    step_price = models.ForeignKey(
        StepPrice, on_delete=models.CASCADE, null=True, verbose_name="StepPrice"
    )
    step_price_percent = models.FloatField(
        null=True, blank=True, verbose_name="StepPricePercent"
    )
    price_reduction = models.TextField(
        null=True, blank=True, verbose_name="PriceReduction"
    )
    participants = models.TextField(null=True, blank=True, verbose_name="Participants")
    advance = models.FloatField(null=True, blank=True, verbose_name="Advance")
    trade_object_html = models.TextField(
        null=True, blank=True, verbose_name="TradeObjectHtml"
    )
    advance_percent = models.FloatField(
        null=True, blank=True, verbose_name="AdvancePercent"
    )
    concours = models.TextField(null=True, blank=True, verbose_name="Concours")
    payment_info = models.TextField(null=True, blank=True, verbose_name="PaymentInfo")
    sale_agreement = models.TextField(
        null=True, blank=True, verbose_name="SaleAgreement"
    )
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, null=True, verbose_name="Classification"
    )


class Participant(models.Model):
    participant_person = models.ForeignKey(
        ParticipantPerson, on_delete=models.CASCADE, null=True, verbose_name="ParticipantPerson"
    )
    participant_company = models.ForeignKey(
        ParticipantCompany, on_delete=models.CASCADE, null=True, verbose_name="ParticipantCompany"
    )

    def __str__(self):
        return f"{self.participant_person}{self.participant_company}"


class SetAnnulment(models.Model):
    annulment_message = models.ForeignKey(
        AnnullmentMessage, null=True, on_delete=models.CASCADE, verbose_name="AnnulmentMessage"
    )

    def __str__(self):
        return self.annulment_message


class SuccessTradeResult(models.Model):
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    substantiation = models.TextField(
        null=True, blank=True, verbose_name="Substantiation"
    )
    winner_person = models.ForeignKey(
        WinnerPerson, on_delete=models.CASCADE, null=True, verbose_name="WinnerPerson"
    )
    winner_company = models.ForeignKey(
        WinnerCompany, on_delete=models.CASCADE, null=True, verbose_name="WinnerCompany"
    )

    def __str__(self):
        return f"{self.price} {self.substantiation} {self.winner_person} {self.winner_company}"


class TradeOrganizer(models.Model):
    trade_organizer_person = models.ForeignKey(
        TradeOrganizerPerson,
        on_delete=models.CASCADE,
        verbose_name="TradeOgranizerPerson",
        null=True,
    )
    trade_organizer_company = models.ForeignKey(
        TradeOrganizerCompany,
        on_delete=models.CASCADE,
        verbose_name="TradeOrganizerCompany",
        null=True,
    )

    def __str__(self):
        return f"{self.trade_organizer_person}{self.trade_organizer_company}"


class BankruptcyCreditor(models.Model):
    bankruptcy_creditor_person = models.ForeignKey(
        BankruptcyCreditorPerson,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorCompany",
        null=True,
    )
    bankruptcy_creditor_company = models.ForeignKey(
        BankruptcyCreditorCompany,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorCompany",
        null=True,
    )
    creditor_lot_number_list = models.ForeignKey(
        CreditorLotNumberList,
        on_delete=models.CASCADE,
        verbose_name="CreditorLotNumberList",
        null=True,
    )

    def __str__(self):
        return f"{self.bankruptcy_creditor_person} {self.bankruptcy_creditor_company} {self.creditor_lot_number_list}"


class LotContractSale(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    contract_info = models.ForeignKey(
        ContractInfo, on_delete=models.CASCADE, null=True, verbose_name="LotNumber"
    )
    contract_participant = models.ForeignKey(
        ContractParticipantList,
        on_delete=models.CASCADE,
        verbose_name="ContractParticipantList",
        null=True,
    )
    additional_info = models.ForeignKey(
        AdditionalInfo, on_delete=models.CASCADE, null=True, verbose_name="AdditionalInfo"
    )

    def __str__(self):
        return f"{self.lot_number} {self.contract_info} {self.contract_participant} {self.additional_info}"


class LotStatistic(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    entry_count = models.IntegerField(blank=True, null=True, verbose_name="EntryCount")
    accept_count = models.IntegerField(
        blank=True, null=True, verbose_name="AcceptCount"
    )
    application_list = models.ForeignKey(
        ApplicationList, on_delete=models.CASCADE, null=True, verbose_name="ApplicationList"
    )

    def __str__(self):
        return f"{self.lot_number} {self.entry_count} {self.accept_count} {self.application_list}"


class Participants(models.Model):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, null=True, verbose_name="Participant"
    )

    def __str__(self):
        return self.participant


class SetBiddingProcessInfo(models.Model):
    bidding_process_info = models.ForeignKey(
        BiddingProcessInfo, null=True, on_delete=models.CASCADE, verbose_name="BiddingProcessInfo"
    )

    def __str__(self):
        return self.bidding_process_info


class BankruptcyCreditorList(models.Model):
    bankruptcy_creditor = models.ForeignKey(
        BankruptcyCreditor, null=True, on_delete=models.CASCADE, verbose_name="BankruptcyCreditor"
    )

    def __str__(self):
        return self.bankruptcy_creditor


class LotContractSaleList(models.Model):
    lot_contract_sale = models.ForeignKey(
        LotContractSale, null=True, on_delete=models.CASCADE, verbose_name="LotContractSale"
    )

    def __str__(self):
        return self.lot_contract_sale


class LotTradeResult(models.Model):
    lot_number = models.IntegerField(blank=True, null=True, verbose_name="LotNumber")
    success_trade_result = models.ForeignKey(
        SuccessTradeResult, null=True, on_delete=models.CASCADE, verbose_name="SuccesTradeResult"
    )
    failure_trade_result = models.ForeignKey(
        FailureTradeResult, null=True, on_delete=models.CASCADE, verbose_name="FailureTradeResult"
    )
    participants = models.ForeignKey(
        Participants, null=True, on_delete=models.CASCADE, verbose_name="Participants"
    )

    def __str__(self):
        return f"{self.lot_number} {self.success_trade_result} {self.failure_trade_result} {self.participants}"


class BiddingEndBankruptcyCreditor(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(blank=True, null=True, verbose_name="EventTime")
    bankruptcy_creditor_list = models.ForeignKey(
        BankruptcyCreditorList,
        on_delete=models.CASCADE,
        verbose_name="BankruptcyCreditorList",
    )
    information = models.ForeignKey(
        Information, null=True, on_delete=models.CASCADE, verbose_name="Information"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.bankruptcy_creditor_list} {self.information}"


class ContractSale(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(blank=True, null=True, verbose_name="EventTime")
    lot_contract_sale_list = models.ForeignKey(
        LotContractSaleList,
        on_delete=models.CASCADE,
        verbose_name="LotContractSaleList",
        null=True,
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_contract_sale_list}"


class LotList(models.Model):
    lot = models.ForeignKey(Lot, null=True, on_delete=models.CASCADE, verbose_name="Lot")
    lot_statistic = models.ForeignKey(
        LotStatistic, on_delete=models.CASCADE, null=True, verbose_name="LotStatistic"
    )
    bidding_state_lot_info = models.ForeignKey(
        BiddingStateLotInfo, on_delete=models.CASCADE, null=True, verbose_name="LotStatistic"
    )
    lot_trade_result = models.ForeignKey(
        LotTradeResult, on_delete=models.CASCADE, null=True, verbose_name="LotTradeResult"
    )
    lot_info = models.ForeignKey(
        LotInfo, on_delete=models.CASCADE, null=True, verbose_name="LotInfo"
    )
    nil = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.lot}{self.lot_statistic}{self.bidding_state_lot_info} {self.lot_trade_result} {self.lot_info} {self.nil}"


class ApplicationSessionEnd(models.Model):
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.event_time}{self.trade_id}{self.lot_list}"


class ApplicationSessionStart(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id}{self.event_time}{self.lot_list}"


class ApplicationSessionStatistic(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    date_begin = models.DateField(null=True, blank=True, verbose_name="DateBegin")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList", blank=True,
    )
    attach = models.ForeignKey(Attach, null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list} {self.attach}"


class BiddingCancel(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingEnd(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list}"


class BiddingFail(models.Model):
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach, null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.reason} {self.trade_id} {self.event_time} {self.lot_list} {self.attach}"


class BiddingPause(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList, null=True, on_delete=models.CASCADE, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingResult(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE, null=True, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach, null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list} {self.attach}"


# class SetBiddingResult(models.Model):
#
#     bidding_result = models.ForeignKey(BiddingResult,null=True,on_delete=models.CASCADE,verbose_name="BiddingResult")


class BiddingResume(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    reason = models.TextField(null=True, blank=True, verbose_name="Reason")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE, null=True, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.reason} {self.lot_list}"


class BiddingStart(models.Model):
    trade_id = models.TextField(null=True, blank=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE, null=True, verbose_name="LotList"
    )

    def __str__(self):
        return f"{self.trade_id} {self.event_time} {self.lot_list}"


class SetBiddingEndBankruptcyCreditor(models.Model):
    bidding_end_bankruptcy_creditor = models.ForeignKey(
        BiddingEndBankruptcyCreditor,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="BiddingEndBankruptcyCreditor",
    )

    def __str__(self):
        return self.bidding_end_bankruptcy_creditor


class SetContractSale(models.Model):
    contract_sale = models.ForeignKey(
        ContractSale, null=True, on_delete=models.CASCADE, verbose_name="ContractSale"
    )

    def __str__(self):
        return self.contract_sale


class TradeInfo(models.Model):
    auction_type = models.TextField(null=True, blank=True, verbose_name="AuctionType")
    form_price = models.TextField(null=True, blank=True, verbose_name="FormPrice")
    isrepeat = models.BooleanField(null=True, blank=True, verbose_name="ISRepeat")
    close_form = models.ForeignKey(
        CloseForm, null=True, on_delete=models.CASCADE, verbose_name="CloseForm"
    )
    date_publish_smi = models.ForeignKey(
        DatePublishSmi, null=True, on_delete=models.CASCADE, verbose_name="DatePublishSMI"
    )
    date_publish_efir = models.DateTimeField(
        null=True, blank=True, verbose_name="DatePublishEFIR"
    )
    open_form = models.ForeignKey(
        OpenForm, on_delete=models.CASCADE, null=True, verbose_name="OpenForm"
    )
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, null=True, verbose_name="Application"
    )
    lot_list = models.ForeignKey(
        LotList, on_delete=models.CASCADE, null=True, verbose_name="LotList"
    )
    attach = models.ForeignKey(Attach, null=True, on_delete=models.CASCADE, verbose_name="Attach")

    def __str__(self):
        return (
            f"{self.auction_type} {self.form_price} "
            f"{self.isrepeat} {self.close_form} {self.date_publish_smi} "
            f"{self.date_publish_efir} {self.open_form}{self.application}{self.lot_list}{self.attach}"
        )


class BiddingInvitation(models.Model):
    trade_id = models.TextField(blank=True, null=True, verbose_name="TradeId")
    event_time = models.DateTimeField(null=True, blank=True, verbose_name="EventTime")
    idefrsb = models.TextField(null=True, blank=True, verbose_name="IDEFRSB")
    debtor = models.ForeignKey(Debtor, null=True, on_delete=models.CASCADE, verbose_name="Debtor")
    legal_case = models.ForeignKey(
        LegalCase, on_delete=models.CASCADE, null=True, verbose_name="LegalCase"
    )
    company_bankr_commis = models.ForeignKey(
        CompanyBankrCommis, on_delete=models.CASCADE, null=True, verbose_name="CompanyBankrCommis"
    )
    arbitr_manager = models.ForeignKey(
        ArbitrManager, on_delete=models.CASCADE, null=True, verbose_name="ArbitrManager"
    )
    trade_ogranizer = models.ForeignKey(
        TradeOrganizer, on_delete=models.CASCADE, null=True, verbose_name="TradeOrganizer"
    )
    trade_info = models.ForeignKey(
        TradeInfo, on_delete=models.CASCADE, null=True, verbose_name="TradeInfo"
    )

    def __str__(self):
        return (
            f"{self.trade_id} {self.event_time} "
            f"{self.idefrsb} {self.debtor} {self.legal_case} "
            f"{self.company_bankr_commis} {self.arbitr_manager}{self.trade_ogranizer}{self.trade_info}")


class SetApplicationSessionEnd(models.Model):
    application_session_end = models.ForeignKey(
        ApplicationSessionEnd,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionEnd",
    )

    def __str__(self):
        return self.application_session_end


class SetApplicationSessionStart(models.Model):
    application_session_start = models.ForeignKey(
        ApplicationSessionStart,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionStart",
    )

    def __str__(self):
        return self.application_session_start


class SetApplicationSessionStatistic(models.Model):
    application_session_statistic = models.ForeignKey(
        ApplicationSessionStatistic,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="ApplicationSessionStatistic",
    )

    def __str__(self):
        return self.application_session_statistic


class SetBiddingCancel(models.Model):
    bidding_cancel = models.ForeignKey(
        BiddingCancel, null=True, on_delete=models.CASCADE, verbose_name="BiddingCancel"
    )

    def __str__(self):
        return self.bidding_cancel


class SetBiddingEnd(models.Model):
    bidding_end = models.ForeignKey(
        BiddingEnd, null=True, on_delete=models.CASCADE, verbose_name="BiddingEnd"
    )

    def __str__(self):
        return self.bidding_end


class SetBiddingFail(models.Model):
    bidding_fail = models.ForeignKey(
        BiddingFail, null=True, on_delete=models.CASCADE, verbose_name="BiddingFail"
    )

    def __str__(self):
        return self.bidding_fail


class SetBiddingPause(models.Model):
    bidding_pause = models.ForeignKey(
        BiddingPause, null=True, on_delete=models.CASCADE, verbose_name="BiddingPause"
    )

    def __str__(self):
        return self.bidding_pause


class SetBiddingResult(models.Model):
    bidding_result = models.ForeignKey(
        BiddingResult, null=True, on_delete=models.CASCADE, verbose_name="BiddingResult"
    )

    def __str__(self):
        return self.bidding_result


class SetBiddingResume(models.Model):
    bidding_resume = models.ForeignKey(
        BiddingResume, null=True, on_delete=models.CASCADE, verbose_name="BiddingResume"
    )

    def __str__(self):
        return self.bidding_resume


class SetBiddingStart(models.Model):
    bidding_start = models.ForeignKey(
        BiddingStart, null=True, on_delete=models.CASCADE, verbose_name="BiddingStart"
    )

    def __str__(self):
        return self.bidding_start


class SetBiddingInvitation(models.Model):
    bidding_invitations = models.ForeignKey(
        BiddingInvitation, null=True, on_delete=models.CASCADE, verbose_name="BiddingInvitation"
    )

    def __str__(self):
        return self.bidding_invitations


class Body(models.Model):
    set_bidding_process_info = models.ForeignKey(
        SetBiddingProcessInfo,
        on_delete=models.CASCADE,
        verbose_name="SetBiddingProcessInfo",
        null=True,
    )
    set_application_session_start = models.ForeignKey(
        SetApplicationSessionStart,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionStart",
    )
    set_application_session_end = models.ForeignKey(
        SetApplicationSessionEnd,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionEnd",
    )
    set_application_session_statistic = models.ForeignKey(
        SetApplicationSessionStatistic,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetApplicationSessionStatistic",
    )
    set_bidding_fail = models.ForeignKey(
        SetBiddingFail, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingFail"
    )
    set_bidding_invitation = models.ForeignKey(
        SetBiddingInvitation,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="SetBiddingInvitation",
    )
    set_contract_sale = models.ForeignKey(
        SetContractSale, null=True, on_delete=models.CASCADE, verbose_name="SetContractSale"
    )
    set_bidding_result = models.ForeignKey(
        SetBiddingResult, null=True, on_delete=models.CASCADE, verbose_name="SetBuddingResult"
    )

    set_bidding_end = models.ForeignKey(
        SetBiddingEnd, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingEnd"
    )

    set_bidding_start = models.ForeignKey(
        SetBiddingStart, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingStart"
    )

    set_bidding_cancel = models.ForeignKey(
        SetBiddingCancel, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingCancel"
    )
    set_bidding_pause = models.ForeignKey(
        SetBiddingPause, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingPause"
    )
    set_annulment = models.ForeignKey(
        SetAnnulment, null=True, on_delete=models.CASCADE, verbose_name="SetAnnulment"
    )
    set_bidding_end_bankruptcy_creditor = models.ForeignKey(
        SetBiddingEndBankruptcyCreditor,
        on_delete=models.CASCADE,
        verbose_name="set_bidding_end_bankruptcy_creditor",
        null=True,
    )
    set_bidding_resume = models.ForeignKey(
        SetBiddingResume, null=True, on_delete=models.CASCADE, verbose_name="SetBiddingResume"
    )


class Envelope(models.Model):
    body = models.ForeignKey(Body, null=True, on_delete=models.CASCADE, verbose_name="Body")

    # w3_org_2003_05_soap_envelope_body = models.ForeignKey(Body, on_delete=models.CASCADE, verbose_name="Body",related_name="w3_body")

    def __str__(self):
        return f"{self.body}"


class BankruptSupervisoryPerson(models.Model):
    bankrupt_supervisory_person = models.TextField(blank=True, null=True)
    responsibility_amount = models.FloatField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    code_type = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    is_arraignment = models.BooleanField(blank=True, null=True)


class BankruptSupervisoryPersons(models.Model):
    bankrupt_supervisory_person = models.ForeignKey(BankruptSupervisoryPerson, null=True, blank=True,
                                                    on_delete=models.CASCADE)


class Message(models.Model):
    envelope = models.ForeignKey(
        Envelope, null=True, on_delete=models.CASCADE, verbose_name="Envelope"
    )
    # w3_org_2003_05_soap_envelope_envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE,
    #
    #                                                          verbose_name="Envelope")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, blank=True, null=True,
                                                     on_delete=models.CASCADE)
    number = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return (
            f"{self.envelope}"
            """{self.w3_org_2003_05_soap_envelope_envelope}"""
        )


class Trade(models.Model):
    id_efrsb = models.IntegerField(null=True, blank=True, verbose_name="ID_EFRSB")
    id_external = models.TextField(null=True, blank=True, verbose_name="ID_External")
    message = models.ForeignKey(
        Message, null=True, on_delete=models.CASCADE, verbose_name="Message"
    )


class TradeList(models.Model):
    trade = models.ForeignKey(Trade, null=True, on_delete=models.CASCADE, verbose_name="Trade")


class TradePlace(models.Model):
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    trade_list = models.ForeignKey(
        TradeList, null=True, on_delete=models.CASCADE, verbose_name="TradeList"
    )


class TradePlaceList(models.Model):
    trade_place = models.ForeignKey(
        TradePlace, null=True, on_delete=models.CASCADE, verbose_name="TradeList"
    )


# ============================================================================================


class GetMessageContent(models.Model):
    get_message_content_id = models.IntegerField(null=True, blank=True, verbose_name="Идентификатор сообщения в ЕФРСБ")


class GetDebtorMessagesContentForPeriodByIdBankrupt(models.Model):
    id_Bankrupt = models.BigIntegerField(blank=True, null=True, verbose_name="Идентификатор должника")
    startDate = models.DateTimeField(blank=True, null=True, verbose_name="Дата начала периода")


class FirmTradeOrganizer(models.Model):
    full_name = models.CharField(max_length=1024, blank=True, verbose_name="FullName")
    short_name = models.CharField(max_length=512, blank=True, verbose_name="ShortName")
    post_address = models.CharField(max_length=300, blank=True, verbose_name="PostAddress")
    legal_address = models.CharField(max_length=300, blank=True, verbose_name="LegalAddress")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")
    okpo = models.CharField(max_length=8, blank=True, verbose_name="OKPO")


class FirmTradeOrganizerAgent(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    firm_trade_organizer = models.ForeignKey(FirmTradeOrganizer, blank=True, verbose_name="FirmTradeOrganizer",
                                             on_delete=models.CASCADE)


class SroInfo(models.Model):
    inn = models.CharField(max_length=15, blank=True, verbose_name="INN")
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    legal_address = models.CharField(max_length=1024, blank=True, verbose_name="LegalAddress")
    post_address = models.CharField(max_length=1024, blank=True, verbose_name="PostAddress")


class OperatorSro(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    sro_info = models.ForeignKey(SroInfo, blank=True, verbose_name="SroInfo", on_delete=models.CASCADE)


class PersonTradeOrganizer(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    address = models.CharField(max_length=300, blank=True, verbose_name="Address")
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
    ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")


class ForeignSystem(models.Model):
    name = models.CharField(max_length=256, blank=True, verbose_name="Name")


class Operator(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    organization_name = models.CharField(max_length=50, blank=True, verbose_name="OrganizationName")
    organization_department_name = models.CharField(max_length=200, blank=True,
                                                    verbose_name="OrganizationDepartmentName")


class FnsDepartment(models.Model):
    name = models.CharField(max_length=250, blank=True, verbose_name="Name")
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")


class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")


class Company(models.Model):
    name = models.CharField(max_length=1024, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Fio(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")


class Publisher_Arbitr_Manager_v2(models.Model):
    fio = models.ForeignKey(Fio, null=True, on_delete=models.CASCADE, blank=True)
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
    snils = models.CharField(max_length=11, blank=True, verbose_name="SNILS")
    ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")
    correspondence_address = models.CharField(max_length=300, blank=True, verbose_name="Correspondence Address")
    sro = models.ForeignKey(Sro, null=True, on_delete=models.CASCADE, blank=True)


class Publisher_Arbitr_Manager_Sro_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")
    address = models.CharField(max_length=1024, blank=True, verbose_name="Address")


class Publisher_FirmTrade_Organizer_v2(models.Model):
    name = models.CharField(max_length=1024, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher_PersonTrade_Organizer_v2(models.Model):
    fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=True)
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
    ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")


class Publisher_Company_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher_Person_v2(models.Model):
    fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=True)
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")


class Publisher_CentralBankRf_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher_Asv_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher_FnsDepartment_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher_Efrsb_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")


class Publisher_Mfc_v2(models.Model):
    name = models.CharField(max_length=512, blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")


class Publisher(models.Model):
    xsi_type = models.CharField(max_length=30, blank=True,null=True, verbose_name="Publisher")  # xsi:type
    publisher_arbitr_manager_v2 = models.ForeignKey(Publisher_Arbitr_Manager_v2, on_delete=models.CASCADE,null=True, blank=True)
    publisher_arbitr_manager_sro_v2 = models.ForeignKey(Publisher_Arbitr_Manager_Sro_v2, on_delete=models.CASCADE,
                                                        blank=True, null=True)
    publisher_firmtrade_organizer_v2 = models.ForeignKey(Publisher_FirmTrade_Organizer_v2, on_delete=models.CASCADE,
                                                         blank=True, null=True)
    publisher_persontrade_organizer_v2 = models.ForeignKey(Publisher_PersonTrade_Organizer_v2, on_delete=models.CASCADE,
                                                           blank=True, null=True)
    publisher_company_v2 = models.ForeignKey(Publisher_Company_v2, on_delete=models.CASCADE, blank=True, null=True)
    publisher_person_v2 = models.ForeignKey(Publisher_Person_v2, on_delete=models.CASCADE, blank=True, null=True)
    publisher_centralbankrf_v2 = models.ForeignKey(Publisher_CentralBankRf_v2, on_delete=models.CASCADE, blank=True,
                                                   null=True)
    publisher_asv_v2 = models.ForeignKey(Publisher_Asv_v2, on_delete=models.CASCADE, blank=True, null=True)
    publisher_fnsdepartment_v2 = models.ForeignKey(Publisher_FnsDepartment_v2, on_delete=models.CASCADE, blank=True,
                                                   null=True)
    publisher_efrsb_v2 = models.ForeignKey(Publisher_Efrsb_v2, on_delete=models.CASCADE, blank=True, null=True)
    publisher_mfc_v2 = models.ForeignKey(Publisher_Mfc_v2, on_delete=models.CASCADE, blank=True, null=True)


class NameHistoryItem(models.Model):
    name_history_item = models.CharField(max_length=1500, verbose_name="NameHistoryItem")


class BankruptPerson(models.Model):
    insolvent_catrory_name = models.CharField(max_length=100, blank=True, verbose_name="InsolventCategoryName")
    first_name = models.CharField(max_length=50, blank=True, verbose_name="FirstName")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="MiddleName")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="LastName")
    ogrnip = models.CharField(max_length=15, blank=True, verbose_name="OGRNIP")
    address = models.CharField(max_length=300, blank=True, verbose_name="Address")
    inn = models.CharField(max_length=12, blank=True, verbose_name="INN")
    snils = models.CharField(max_length=11, blank=True, verbose_name="SNILS")
    birth_date = models.DateTimeField(blank=True, verbose_name="BirthDate")
    birth_place = models.CharField(max_length=300, blank=True, verbose_name="BirthPlace")
    name_history = models.ForeignKey(NameHistoryItem, on_delete=models.CASCADE, verbose_name="NameHistory")


class BankruptFirm(models.Model):
    insolvent_catrory_name = models.CharField(max_length=100, blank=True, verbose_name="InsolventCategoryName")
    inn = models.CharField(max_length=10, blank=True, verbose_name="INN")
    full_name = models.CharField(max_length=1024, blank=True, verbose_name="FullName")
    short_name = models.CharField(max_length=512, blank=True, verbose_name="ShortName")
    post_address = models.CharField(max_length=300, blank=True, verbose_name="PostAddress")
    legal_addres = models.CharField(max_length=300, blank=True, verbose_name="LegalAddress")
    ogrn = models.CharField(max_length=13, blank=True, verbose_name="OGRN")
    okpo = models.CharField(max_length=8, blank=True, verbose_name="OKPO")


class BankruptInfo(models.Model):
    bankrupt_type = models.CharField(max_length=30, blank=True, verbose_name="BankruptType")
    bankrupt_category = models.CharField(max_length=50, blank=True, verbose_name="BankruptCategory")
    bankruptfirm = models.ForeignKey(BankruptFirm, on_delete=models.CASCADE, blank=True,
                                     verbose_name="BankruptFirm")
    bankrupt_person = models.ForeignKey(BankruptPerson, on_delete=models.CASCADE, blank=True,
                                        verbose_name="BankruptPerson")


class Category(models.Model):
    code = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Bankrupt_Company_v2(models.Model):
    category = models.ForeignKey(Category,null=True,  on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=1024,null=True,  blank=True, verbose_name="Name")
    ogrn = models.CharField(max_length=13,null=True,  blank=True, verbose_name="OGRNIP")
    inn = models.CharField(max_length=10,null=True,  blank=True, verbose_name="INN")
    address = models.CharField(max_length=300,null=True,  blank=True, verbose_name="Address")


class FioHistory(models.Model):
    fio = models.ForeignKey(Fio, on_delete=models.CASCADE, blank=True)


class Bankrupt_Person_v2(models.Model):
    category = models.ForeignKey(Category,null=True,  on_delete=models.CASCADE, blank=True)
    fio = models.ForeignKey(Fio,null=True,  on_delete=models.CASCADE, blank=True)
    inn = models.CharField(max_length=12,null=True,  blank=True, verbose_name="INN")
    snils = models.CharField(max_length=11,null=True,  blank=True, verbose_name="SNILS")
    address = models.CharField(max_length=300,null=True,  blank=True, verbose_name="Address")
    birth_date = models.TextField(blank=True,null=True,  verbose_name="BirthDate")
    birth_place = models.CharField(max_length=300,null=True, blank=True, verbose_name="BirthPlace")
    fio_history = models.ForeignKey(FioHistory,null=True,blank=True, on_delete=models.CASCADE, verbose_name="FioHistory")


class FileInfo(models.Model):
    name = models.TextField(null=True, verbose_name="Name")
    hash = models.TextField(null=True, verbose_name="Hash")


class FileInfoList(models.Model):
    file_info = models.ForeignKey(FileInfo,null=True,  on_delete=models.CASCADE)


class Bankrupt(models.Model):
    bankrupt = models.CharField(max_length=30,null=True,  blank=True, verbose_name="Bankrupt")
    bankrupt_company_v2 = models.ForeignKey(Bankrupt_Company_v2,null = True, on_delete=models.CASCADE, blank=True)
    bankrupt_person_v2 = models.ForeignKey(Bankrupt_Person_v2,null=True, on_delete=models.CASCADE, blank=True)


class MessageUrl(models.Model):
    url_name = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    download_size = models.CharField(null=True, max_length=15, blank=True)


class MessageURLList(models.Model):
    message_url = models.ForeignKey(MessageUrl, on_delete=models.CASCADE)


class PublisherInfo(models.Model):
    publisher_type = models.CharField(max_length=30, blank=True, verbose_name="PublisherType")
    arbitr_manager = models.ForeignKey(ArbitrManager, blank=True, on_delete=models.CASCADE,
                                       verbose_name="ArbitrManager")
    person_trade_organizer = models.ForeignKey(PersonTradeOrganizer, on_delete=models.CASCADE,
                                               verbose_name="PersonTradeOrganizer")
    firm_trade_organizer = models.ForeignKey(FirmTradeOrganizer, blank=True, on_delete=models.CASCADE,
                                             verbose_name="FirmTradeOrganizer")
    foreign_system = models.ForeignKey(ForeignSystem, blank=True, on_delete=models.CASCADE,
                                       verbose_name="ForeingSystem")
    operator_sro = models.ForeignKey(OperatorSro, blank=True, on_delete=models.CASCADE, verbose_name="OperatorSro")
    operator_cbrf = models.ForeignKey(Operator, blank=True, on_delete=models.CASCADE, verbose_name="Operator")
    fns_department = models.ForeignKey(FnsDepartment, blank=True, on_delete=models.CASCADE,
                                       verbose_name="FnsDepartment")
    person = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE, verbose_name="Person")
    company = models.ForeignKey(Company, blank=True, on_delete=models.CASCADE, verbose_name="Company")


class DecisionType(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    Id = models.BigIntegerField(blank=True,null=True)


class CourtDecree(models.Model):
    court_id = models.TextField(blank=True, null=True)
    court_name = models.TextField(blank=True, null=True, verbose_name="CourtName")
    file_number = models.TextField(blank=True, null=True, verbose_name="FileNumber")
    decision_date = models.DateTimeField(blank=True, null=True, verbose_name="DecisionDate")


class ArbitrManagerInfo(models.Model):
    Id = models.BigIntegerField(blank=True,null=True)
    registry_number = models.TextField(blank=True, null=True, verbose_name="RegistryNumber")
    first_name = models.TextField(blank=True, null=True, verbose_name="FirstName")
    middle_name = models.TextField(blank=True, null=True, verbose_name="MiddleName")
    last_name = models.TextField(blank=True, null=True, verbose_name="LastName")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")
    snils = models.TextField(blank=True, null=True, verbose_name="SNILS")


class LegalCaseTerminationType(models.Model):
    code = models.TextField(blank=True, null=True, verbose_name="Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")


class ProcedureProlongation(models.Model):
    date = models.DateTimeField(blank=True, null=True, verbose_name="Date")
    months = models.TextField(blank=True, null=True, verbose_name="Months")
    message_number = models.TextField(blank=True, null=True, verbose_name="MessageNumber")


class CanceledMessages(models.Model):
    number = models.TextField(blank=True, null=True, verbose_name="Number")


class AuctionLotClassifier(models.Model):
    code = models.FloatField(blank=True, null=True, verbose_name="Code")
    name = models.TextField(blank=True, null=True, verbose_name="Name")


class AuctionLot(models.Model):
    order = models.TextField(blank=True, null=True, verbose_name="Order")
    start_price = models.FloatField(blank=True, null=True, verbose_name="StartPrice")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    step = models.FloatField(blank=True, null=True, verbose_name="Step")
    advance = models.FloatField(blank=True, null=True, verbose_name="Advance")
    auction_step_unit = models.TextField(blank=True, null=True, verbose_name="AuctionStepUnit")
    advance_step_unit = models.TextField(blank=True, null=True, verbose_name="AdvanceStepUnit")
    price_reduction = models.TextField(blank=True, null=True, verbose_name="PriceReduction")
    classifier_collection = models.ForeignKey(AuctionLotClassifier, blank=True, null=True, on_delete=models.CASCADE)


class LotTable(models.Model):
    auctiot_lot = models.ForeignKey(AuctionLot, blank=True, null=True, on_delete=models.CASCADE)


class Auction(models.Model):
    is_repeat = models.BooleanField(blank=True, null=True, verbose_name="IsRepeat")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Date")
    trade_type = models.TextField(blank=True, null=True, verbose_name="TradeType")
    price_type = models.TextField(blank=True, null=True, verbose_name="PriceType")
    trade_site = models.TextField(blank=True, null=True, verbose_name="TradeSite")
    id_trade_place = models.TextField(blank=True, null=True, verbose_name="IdTradePlace")
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    additional_text = models.TextField(blank=True, null=True, verbose_name="AdditionalText")
    lot_table = models.ForeignKey(LotTable, blank=True, null=True, verbose_name="LotTable", on_delete=models.CASCADE)
    application = models.ForeignKey(Application, blank=True, null=True, verbose_name="Application",
                                    on_delete=models.CASCADE)


class CourtDecision(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    losses_from_arbitr_manager_actions_amount = models.TextField(blank=True, null=True,
                                                                 verbose_name="LossesFromArbitrManagerActionsAmmount")
    citizen_not_released_from_responsibility = models.TextField(blank=True, null=True,
                                                                   verbose_name="CitizenNotReleasedFromResponsibility")
    arbitrmanager_illegal_actiontype = models.TextField(blank=True, null=True,
                                                        verbose_name="ArbitrManagerIllegalActionType")
    decision_made_due_tor_cancellation_restructuring_plan = models.TextField(blank=True, null=True,
                                                                                verbose_name="DecisionMadeDueTorCancellationRestructuringPlan")
    reason_for_cancellation_restructuring_plan = models.TextField(blank=True, null=True,
                                                                  verbose_name="ReasonForCancellationRestructuringPlan")
    creditor_claim_register_close_date = models.TextField(blank=True, null=True,
                                                              verbose_name="CreditorClaimRegisterCloseDate")
    creditor_claim_setting_requirement_expiration_date = models.TextField(blank=True, null=True,
                                                                              verbose_name="CreditorClaimSettingRequirementsExpirationDate")
    arbitrmanager_type = models.TextField(blank=True, null=True, verbose_name="ArbitrManagerType")
    decision_type = models.ForeignKey(DecisionType, blank=True, null=True, on_delete=models.CASCADE)
    court_decree = models.ForeignKey(CourtDecree, blank=True, null=True, on_delete=models.CASCADE)
    arbitrmanager_info = models.ForeignKey(ArbitrManagerInfo, blank=True, null=True, on_delete=models.CASCADE)
    legal_case_termination_type = models.ForeignKey(LegalCaseTerminationType, blank=True, null=True,
                                                    on_delete=models.CASCADE)
    procedure_prolongation = models.ForeignKey(ProcedureProlongation, blank=True, null=True, on_delete=models.CASCADE)
    changed_message_number = models.TextField(blank=True, null=True, verbose_name="ChangedMessageNumber")
    canceled_messages = models.ForeignKey(CanceledMessages, blank=True, null=True, on_delete=models.CASCADE)
    next_court_session_date = models.TextField(blank=True, null=True, verbose_name="NextCourtSessionDate")
    meeting_form = models.TextField(blank=True, null=True, verbose_name="MeetingForm")
    web_address = models.TextField(blank=True, null=True, verbose_name="WebAddress")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")
    fu_mail_address = models.TextField(blank=True, null=True, verbose_name="FuMailAddress")


class Director(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    id_arbitr_manager = models.TextField(blank=True, null=True, verbose_name="IdAritrManager")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    snils = models.TextField(blank=True, null=True, verbose_name="SNILS")
    sro = models.ForeignKey(Sro, blank=True, null=True, verbose_name="SRO", on_delete=models.CASCADE)


class ChangeAdministration(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    decision_name = models.TextField(blank=True, null=True, verbose_name="DecisionName")
    decision_date = models.DateTimeField(blank=True, null=True, verbose_name="DecisionDate")
    decision_number = models.TextField(blank=True, null=True, verbose_name="DecisionNumber")
    director = models.ForeignKey(Director, blank=True, null=True, verbose_name="Director", on_delete=models.CASCADE)


class Other(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class TerminationAdministraion(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    decision_name = models.TextField(blank=True, null=True, verbose_name="DecisionName")
    decision_date = models.DateTimeField(blank=True, null=True, verbose_name="DecisionDate")
    decision_number = models.TextField(blank=True, null=True, verbose_name="DecisionNumber")
    cause = models.TextField(blank=True, null=True)
    other_cause_description = models.TextField(blank=True, null=True)
    director = models.ForeignKey(Director, blank=True, null=True, on_delete=models.CASCADE)


class AppointAdministration(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    decision_name = models.TextField(blank=True, null=True, verbose_name="DecisionName")
    decision_date = models.DateTimeField(blank=True, null=True, verbose_name="DecisionDate")
    decision_number = models.TextField(blank=True, null=True, verbose_name="DecisionNumber")
    administration_date_from = models.DateTimeField(blank=True, null=True)
    reasons = models.TextField(blank=True, null=True, verbose_name="Reasons")
    members = models.TextField(blank=True, null=True, verbose_name="Members")
    administration_period = models.TextField(blank=True, null=True, verbose_name="AdministrationPeriod")
    authority_credentionals_limitation = models.TextField(blank=True, null=True,
                                                          verbose_name="AuthorityCredentionalsLimitation")
    director = models.ForeignKey(Director, blank=True, null=True, verbose_name="Director", on_delete=models.CASCADE)


class Annul(models.Model):
    text = models.TextField(blank=True, null=True)
    id_addulmnent_message = models.BigIntegerField(blank=True, null=True)
    lock_annuled_message_reason = models.TextField(blank=True, null=True)


class PropertyInventoryResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class PropertyEvaluationReport(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class FailureWinnerInfo(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")


class PurchaserInfo(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")


class SaleContractInfo(models.Model):
    type_sale_contract_info = models.TextField(blank=True, null=True)
    lot_number = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    failure_winner_info = models.ForeignKey(FailureWinnerInfo, null=True, blank=True, on_delete=models.CASCADE)
    conclusion_info = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    conclusion_date = models.DateTimeField(blank=True, null=True)
    property_purchase_price = models.FloatField(blank=True, null=True)


class Contracts(models.Model):
    contracts = models.ForeignKey(SaleContractInfo, blank=True, null=True, on_delete=models.CASCADE)


class SaleContractResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    sale_contract_result_type = models.TextField(blank=True, null=True)
    date_contract = models.DateTimeField(blank=True, null=True, verbose_name="DateContract")
    price = models.FloatField(blank=True, null=True)
    failure_winner_info = models.ForeignKey(FailureWinnerInfo, on_delete=models.CASCADE, null=True, blank=True)
    purchaser_info = models.ForeignKey(PurchaserInfo, blank=True, null=True, on_delete=models.CASCADE)


class SaleContractResult2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_auction_message = models.TextField(blank=True, null=True)
    trade_place_name = models.TextField(blank=True, null=True)
    trade_number = models.TextField(blank=True, null=True)
    contracts = models.ForeignKey(Contracts, blank=True, null=True, on_delete=models.CASCADE)


class Committee(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_site = models.TextField(blank=True, null=True)
    meeting_date = models.DateTimeField(blank=True, null=True)


class SaleOrderPledgedProperty(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_date = models.DateTimeField(blank=True, null=True)
    trade_site = models.TextField(blank=True, null=True)
    id_trade_place = models.BigIntegerField(blank=True, null=True)
    lot_table = models.ForeignKey(LotTable, blank=True, null=True, on_delete=models.CASCADE)
    additional_text = models.TextField(blank=True, null=True)


class ReceivingCreditorDemand(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    demand_date = models.DateTimeField(blank=True, null=True)
    demand_sum = models.FloatField(blank=True, null=True)
    creditor_name = models.TextField(blank=True, null=True)
    reason_occurance = models.TextField(blank=True, null=True)


class IntentionCreditOrg(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class LiabilitiesCreditOrg(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class PerformanceCreditOrg(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class BuyingProperty(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class PersonForResponsibility(models.Model):
    fio = models.TextField(blank=True, null=True)
    type_person_responsibility = models.TextField(blank=True, null=True)
    responsibility_amount = models.FloatField(blank=True, null=True)
    is_arraignment = models.BooleanField(blank=True, null=True)


class AnotherPersonsForResponsibility(models.Model):
    person_for_responsibility = models.ForeignKey(PersonForResponsibility, on_delete=models.CASCADE)


class DealParticipant(models.Model):
    deal_participant = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    code_type = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)


class DealParticipants(models.Model):
    deal_participant = models.ForeignKey(DealParticipant, blank=True, null=True, on_delete=models.CASCADE)


class ActDealInvalid(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    deal_invalid_message_id = models.BigIntegerField(null=True, blank=True)
    deal_not_valid = models.BooleanField(blank=True, null=True)
    court_decision_notice_date = models.DateTimeField(blank=True, null=True)
    deal_participants = models.ForeignKey(DealParticipants, blank=True, null=True, on_delete=models.CASCADE)


class DealInfo(models.Model):
    deal_invalid_message_id = models.BigIntegerField(null=True, blank=True)
    deal_invalid_message_date = models.DateTimeField(null=True, blank=True)
    deal_invalid_message_number = models.BigIntegerField(null=True, blank=True)
    deal_not_valid = models.BooleanField(blank=True, null=True)
    deal_participants = models.ForeignKey(DealParticipants, blank=True, null=True, on_delete=models.CASCADE)


# class BankruptSupervisoryPerson(models.Model):..
#     bankrupt_supervisory_person = models.TextField(blank=True,null=True)

class DeclarationPersonSubsidiary(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, blank=True, null=True,
                                                     on_delete=models.CASCADE)


class Deals(models.Model):
    deal_info = models.ForeignKey(DealInfo, blank=True, null=True, on_delete=models.CASCADE)


class ActDealInvalid2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    deal = models.ForeignKey(Deals, blank=True, null=True, on_delete=models.CASCADE)
    court_decision_notice_date = models.DateTimeField(blank=True, null=True)


class DealInvalid(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    is_apply_by_arbitr_manager = models.BooleanField(null=True, blank=True)
    declaration_notice_date = models.DateTimeField(null=True, blank=True)
    declaration_date = models.DateTimeField(null=True, blank=True)
    deal_participants = models.ForeignKey(DealParticipants, blank=True, null=True, on_delete=models.CASCADE)


class ActReviewDealInvalid(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    act_deal_invalid_message_id = models.BigIntegerField(null=True, blank=True)
    deal_not_valid = models.BooleanField(blank=True, null=True)
    deal_participants = models.ForeignKey(DealParticipants, blank=True, null=True, on_delete=models.CASCADE)


class ActInfo(models.Model):
    act_deal_invalid_message_id = models.BigIntegerField(null=True, blank=True)
    act_deal_invalid_message_date = models.DateTimeField(null=True, blank=True)
    act_deal_invalid_message_number = models.TextField(null=True, blank=True)
    deals = models.ForeignKey(Deals, blank=True, null=True, on_delete=models.CASCADE)


class Acts(models.Model):
    act_info = models.ForeignKey(ActInfo, null=True, blank=True, on_delete=models.CASCADE)


class ActReviewDealInvalid2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    court_decision_notice_date = models.DateTimeField(blank=True, null=True)
    acts = models.ForeignKey(Acts, null=True, blank=True, on_delete=models.CASCADE)


class ActPersonDamages(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, blank=True, null=True,
                                                     on_delete=models.CASCADE)
    another_persons_for_responsibility = models.ForeignKey(AnotherPersonsForResponsibility, on_delete=models.CASCADE,
                                                           blank=True, null=True)
    declaration_person_damages_message_id = models.BigIntegerField(blank=True, null=True)


class ActReviewPersonDamages(models.Model):
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    another_persons_for_responsibility = models.ForeignKey(AnotherPersonsForResponsibility, on_delete=models.CASCADE,
                                                           blank=True, null=True)
    act_person_damages_message_id = models.BigIntegerField(blank=True, null=True)


class DeclarationPersonDamages(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, on_delete=models.CASCADE, blank=True,
                                                     null=True)
    another_persons_for_responsibility = models.ForeignKey(AnotherPersonsForResponsibility, on_delete=models.CASCADE,
                                                           blank=True, null=True)


class SetContractResult2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_auction_message = models.BigIntegerField(blank=True, null=True)
    trade_place_name = models.TextField(blank=True, null=True, verbose_name="TradePlaceName")
    trade_number = models.TextField(blank=True, null=True)
    contracts = models.ForeignKey(Contracts, blank=True, null=True, on_delete=models.CASCADE)


class ActPersonSubsidiary(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, on_delete=models.CASCADE, blank=True,
                                                     null=True)
    declaration_person_subsidiary_message_id = models.TextField(blank=True, null=True)


class ActReviewPersonSubsidiary(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    bankrupt_supervisory_persons = models.ForeignKey(BankruptSupervisoryPersons, on_delete=models.CASCADE, blank=True,
                                                     null=True)
    act_person_subsidiary_id = models.TextField(blank=True, null=True)


class MeetingWorker(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_form = models.TextField(blank=True, null=True)
    meeting_date = models.TextField(blank=True, null=True)
    meeting_site = models.TextField(blank=True, null=True)
    ballots_reception_end_date = models.DateTimeField(blank=True, null=True)
    ballots_send_post_address = models.TextField(blank=True, null=True)
    notice = models.TextField(blank=True, null=True)


class MeetingWorkerResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    is_lead_by_arbitrmanager = models.BooleanField(blank=True, null=True)
    meeting_notice_date = models.DateTimeField(blank=True, null=True)
    meeting_date = models.DateTimeField(blank=True, null=True)
    workers_count = models.IntegerField(blank=True, null=True)
    requirement_summ = models.FloatField(blank=True, null=True)


class ViewDraftRestructuringPlan(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    date_end_restructuring_plan_execution = models.DateTimeField(blank=True, null=True)
    place_of_acquaintance = models.TextField(blank=True, null=True)
    included_registry_requirements_not_satisfied = models.BooleanField(blank=True, null=True)
    bankruptcy_acknowledgment_and_start_of_restructuring_messageid = models.BigIntegerField(blank=True,null=True)

class ViewExecRestructuringPlan(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    date_end_restructuring_plan_execution = models.DateTimeField(blank=True, null=True)
    place_of_acquaintance = models.TextField(blank=True, null=True)
    included_registry_requirements_not_satisfied = models.BooleanField(blank=True, null=True)


class LandPlot(models.Model):
    cadastral_number = models.TextField(blank=True, null=True)
    ownership_right_description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True, verbose_name="AdditionalInfo")


class LandPlots(models.Model):
    land_plot = models.ForeignKey(LandPlot, blank=True, null=True, on_delete=models.CASCADE)


class UncompletedBuildingProject(models.Model):
    cadastral_number = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    additional_info = models.TextField(blank=True, null=True, verbose_name="AdditionalInfo")


class CancelAuctionTradeResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_cancelled_message = models.BigIntegerField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)


class CancelDeliberateBankruptcy(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_changed_message = models.BigIntegerField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)


class ChangeAuction(models.Model):
    # Auction!!!
    id_changed_message = models.BigIntegerField(blank=True, null=True)
    change_reason = models.TextField(blank=True, null=True)


class DeliberateBankruptcy(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    deliberate_bankruptcy_signs = models.TextField(blank=True, null=True)
    deliberate_signs_not_searched_reason = models.TextField(blank=True, null=True)
    fake_bankruptcy_signs = models.TextField(blank=True, null=True)
    fake_signs_not_searched_reason = models.TextField(blank=True, null=True)


class ChangeDeliberateBankruptcy(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    deliberate_bankruptcy_signs = models.TextField(blank=True, null=True)
    deliberate_signs_not_searched_reason = models.TextField(blank=True, null=True)
    fake_bankruptcy_signs = models.TextField(blank=True, null=True)
    fake_signs_not_searched_reason = models.TextField(blank=True, null=True)
    id_cancelled_message = models.BigIntegerField(blank=True, null=True)


class ReducingSizeShareCapital(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    charter_capital_sum = models.FloatField(blank=True, null=True)
    normative_act_add_option_date = models.DateTimeField(blank=True, null=True)
    increase_capital_decision_cancelled = models.BooleanField(blank=True, null=True)


class SelectionPurchaserAssets(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class EstimatesCurrentExpenses(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class OrderAndTimingCalculations(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class InformationAboutBankruptcy(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class EstimatesAndUnsoldAssets(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class RemainingAssetsAndRight(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class CreditOrganizationInfo(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")
    acquirer_liabilities_classification_criteria = models.TextField(blank=True, null=True)
    transferred_liabilities_obtaining_order = models.TextField(blank=True, null=True)


class CreditOrganizations(models.Model):
    credit_organization = models.ForeignKey(CreditOrganizationInfo, blank=True, null=True, on_delete=models.CASCADE)


class TransferAssets(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    credit_organizations = models.ForeignKey(CreditOrganizations, blank=True, null=True, on_delete=models.CASCADE)


class ImpendingTransferAssets(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    credit_organizations = models.ForeignKey(CreditOrganizations, blank=True, null=True, on_delete=models.CASCADE)


class InsuranceOrganization(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")


class TransferInsurancePortfolio(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    expected_delivery_date = models.DateTimeField(blank=True, null=True)
    portfolio_transfer_reason = models.TextField(blank=True, null=True)
    authority_limitation_info = models.TextField(blank=True, null=True)
    insurance_organizaion = models.ForeignKey(InsuranceOrganization, blank=True, null=True, on_delete=models.CASCADE)
    bik = models.TextField(blank=True, null=True)


class BankOpenAccountDebtor(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    name = models.TextField(blank=True, null=True, verbose_name="Name")
    inn = models.TextField(blank=True, null=True, verbose_name="INN")
    ogrn = models.TextField(blank=True, null=True, verbose_name="OGRN")


class ProcedureGrantingIndemnity(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    property_indemnity_offer = models.TextField(blank=True, null=True)
    property_familiarization_procedure = models.TextField(blank=True, null=True)
    consest_application_period = models.TextField(blank=True, null=True)


class RightUnsoldAsset(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class TransferResponsibilitiesFund(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class ExtensionAdministration(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class MeetingParticipantsBuilding(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_date = models.DateTimeField(blank=True, null=True)
    meeting_site = models.TextField(blank=True, null=True)
    notice = models.TextField(blank=True, null=True)
    materials_familiarization_order = models.TextField(blank=True, null=True)


class MeetingPartBuildResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class PartBuildMonetaryClaim(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    arbitral_court = models.TextField(blank=True, null=True)
    consequences = models.TextField(blank=True, null=True)


class StartSettlement(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    settlement_start_date = models.DateTimeField(blank=True, null=True)


class ProcessInventoryDebtor(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")


class Rebuttal(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_rebutted_message = models.BigIntegerField(blank=True, null=True)


class CreditorChoiceRightSubsidiary(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    subsidiary_message_id = models.BigIntegerField(blank=True, null=True)
    subsidiary_act_date = models.DateTimeField(blank=True, null=True)


class AccessionDeclarationSubsidiary(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    declaration_person_subsidiary_message_id = models.BigIntegerField(blank=True, null=True)


class Court(models.Model):
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)


class DisqualificationArbitrationManager(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    duration = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    arbitr_manager = models.ForeignKey(ArbitrManager, null=True, blank=True, on_delete=models.CASCADE)

    court = models.ForeignKey(Court, blank=True, null=True, on_delete=models.CASCADE)


class DisqualificationArbitrationManager2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    reason = models.TextField(blank=True, null=True)
    date_begin = models.DateTimeField(blank=True, null=True)
    arbitr_manager = models.ForeignKey(ArbitrManager, null=True, blank=True, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, blank=True, null=True, on_delete=models.CASCADE)
    duration = models.TextField(blank=True, null=True)


class Duration(models.Model):
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)


class ChangeEstimatesCurrentExpenses(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_changed_message = models.BigIntegerField(blank=True, null=True)


class DeclarationPersonSubsidiaryInfoMessages(models.Model):
    message = models.ForeignKey(Message, null=True, blank=True, on_delete=models.CASCADE)


class ActPersonSubsidiary2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    declaration_person_subsidiary_info_message = models.ForeignKey(DeclarationPersonSubsidiaryInfoMessages, blank=True,
                                                                   null=True, on_delete=models.CASCADE)


class Report(models.Model):
    number = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)


class Appraiser(models.Model):
    fio = models.ForeignKey(Fio, blank=True, null=True, on_delete=models.CASCADE)
    inn = models.TextField(blank=True, null=True)
    snils = models.TextField(blank=True, null=True)
    sro = models.ForeignKey(Sro, blank=True, null=True, on_delete=models.CASCADE)


class Appraisers(models.Model):
    appraiser = models.ForeignKey(Appraiser, blank=True, null=True, on_delete=models.CASCADE)


class Classifier(models.Model):
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)


class ObjectOfAssessment(models.Model):
    classifier = models.ForeignKey(Classifier, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date_of_assessment = models.DateTimeField(blank=True, null=True)
    mark_value = models.FloatField(blank=True, null=True)
    balance_value = models.FloatField(blank=True, null=True)


class Expert(models.Model):
    fio = models.ForeignKey(Fio, blank=True, null=True, on_delete=models.CASCADE)
    inn = models.TextField(blank=True, null=True)
    snils = models.TextField(blank=True, null=True)
    sro = models.ForeignKey(Sro, blank=True, null=True, on_delete=models.CASCADE)


class Experts(models.Model):
    expert = models.ForeignKey(Expert, blank=True, null=True, on_delete=models.CASCADE)


class ExpertDecision(models.Model):
    number = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    experts = models.ForeignKey(Experts, blank=True, null=True, on_delete=models.CASCADE)


class ObjectsOfAssessment(models.Model):
    object_of_assessment = models.ForeignKey(ObjectOfAssessment, blank=True, null=True, on_delete=models.CASCADE)


class AssessmentReport(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    report = models.ForeignKey(Report, blank=True, null=True, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    appraisers = models.ForeignKey(Appraisers, null=True, blank=True, on_delete=models.CASCADE)
    objects_of_assessment = models.ForeignKey(ObjectsOfAssessment, blank=True, null=True, on_delete=models.CASCADE)
    expert_decision = models.ForeignKey(ExpertDecision, blank=True, null=True, on_delete=models.CASCADE)


class ActPersonSubsidiaryInfoMessages(models.Model):
    message = models.ForeignKey(Message, null=True, blank=True, on_delete=models.CASCADE)


class ActReviewPersonSubsidiary2(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    act_person_subsidiary_info_messages = models.ForeignKey(ActPersonSubsidiaryInfoMessages, blank=True, null=True,
                                                            on_delete=models.CASCADE)


class MonetaryObligation(models.Model):
    creditor_name = models.TextField(blank=True, null=True)
    creditor_region = models.TextField(blank=True, null=True)
    creditor_location = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    basis = models.TextField(blank=True, null=True)
    total_sum = models.FloatField(blank=True, null=True)
    debt_sum = models.FloatField(blank=True, null=True)
    penalty_sum = models.FloatField(blank=True, null=True)


class Bank(models.Model):
    name = models.TextField(blank=True, null=True)
    bank_identifier = models.IntegerField(blank=True, null=True)


class ObligatoryPayment(models.Model):
    name = models.TextField(blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    penalty_sum = models.FloatField(blank=True, null=True)


class ObligatoryPayments(models.Model):
    obligatory_payment = models.ForeignKey(ObligatoryPayment, blank=True, null=True, on_delete=models.CASCADE)


class MonetaryObligations(models.Model):
    monetary_obligation = models.ForeignKey(MonetaryObligation, blank=True, null=True, on_delete=models.CASCADE)


class ReturnOfApplicationOnExtrajudicialBankruptcy(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    no_return_of_enforcement_documen = models.BooleanField(blank=True, null=True)
    active_enforcement_proceeding = models.BooleanField(blank=True, null=True)


class CreditorsNonFromEntrepreneurship(models.Model):
    monetary_obligations = models.ForeignKey(MonetaryObligations, blank=True, null=True, on_delete=models.CASCADE)
    obligatory_payment = models.ForeignKey(ObligatoryPayment, blank=True, null=True, on_delete=models.CASCADE)
    non_monetary_obligations = models.TextField(blank=True, null=True)


class Banks(models.Model):
    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.CASCADE)


class CreditorsFromEntrepreneurship(models.Model):
    monetary_obligations = models.ForeignKey(MonetaryObligations, blank=True, null=True, on_delete=models.CASCADE)
    obligatory_payment = models.ForeignKey(ObligatoryPayment, blank=True, null=True, on_delete=models.CASCADE)
    non_monetary_obligations = models.TextField(blank=True, null=True)


class StartOfExtrajudicialBankruptcy(models.Model):
    creditors_non_from_entrepreneurship = models.ForeignKey(CreditorsNonFromEntrepreneurship, blank=True, null=True,
                                                            on_delete=models.CASCADE)
    is_individual_entrepreneur = models.BooleanField(blank=True, null=True)
    creditors_from_entrepreneurship = models.ForeignKey(CreditorsFromEntrepreneurship, blank=True, null=True,
                                                        on_delete=models.CASCADE)
    banks = models.ForeignKey(Banks, blank=True, null=True, on_delete=models.CASCADE)


class UncompletedBuildingProjects(models.Model):
    uncompleted_building_project = models.ForeignKey(UncompletedBuildingProject, blank=True, null=True,
                                                     on_delete=models.CASCADE)


class TerminationOfExtrajudicialBankruptcy(models.Model):
    start_of_extrajudicial_bankruptcy_message_number = models.BigIntegerField(blank=True, null=True)
    property_status_changed = models.BooleanField(blank=True, null=True)
    court_decision_issued = models.BooleanField(blank=True, null=True)
    other_reason = models.TextField(blank=True, null=True)


class CompletionOfExtrajudicialBankruptcy(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    start_of_extrajudicial_bankruptcy_message_number = models.BigIntegerField(blank=True, null=True)


class TransferOwnershipRealEstate(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    court_decision_date = models.DateTimeField(blank=True, null=True)
    transfer_ownership_state_registration_date = models.DateTimeField(blank=True, null=True)
    acquirer_name = models.TextField(blank=True, null=True)
    acquirer_address = models.TextField(blank=True, null=True)
    acquirer_ogrn = models.TextField(blank=True, null=True)
    acquirer_inn = models.TextField(blank=True, null=True)
    land_plots = models.ForeignKey(LandPlots, on_delete=models.CASCADE, blank=True, null=True)
    uncompleted_building_projects = models.ForeignKey(UncompletedBuildingProjects, blank=True, null=True,
                                                      on_delete=models.CASCADE)


class BeginExecutoryProcess(models.Model):
    text = models.TextField(blank=True, null=True)
    date_begin_executory_process = models.DateTimeField(blank=True, null=True)
    number_executory_process = models.TextField(blank=True, null=True)


class TransferAssertsForImplementation(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    date_sumbmit = models.DateTimeField(blank=True, null=True)
    number_executory_process = models.TextField(blank=True, null=True)
    id_begin_exe_process_message = models.BigIntegerField(blank=True, null=True)


class MeetingResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_form = models.TextField(null=True, blank=True, verbose_name="MeetingForm")


class Winner(models.Model):
    participant_person = models.ForeignKey(ParticipantPerson, blank=True, null=True, on_delete=models.CASCADE)
    participant_company = models.ForeignKey(ParticipantCompany, blank=True, null=True, on_delete=models.CASCADE)


class Buyer(models.Model):
    participant_person = models.ForeignKey(ParticipantPerson, blank=True, null=True, on_delete=models.CASCADE)
    participant_company = models.ForeignKey(ParticipantCompany, blank=True, null=True, on_delete=models.CASCADE)


class TradeResultLot(models.Model):
    order = models.TextField(blank=True, null=True, verbose_name="Order")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    lot_status = models.TextField(blank=True, null=True, verbose_name="LotStatus")
    basis = models.TextField(blank=True, null=True, verbose_name="Basis")
    winner = models.ForeignKey(Winner, null=True, blank=True, verbose_name="Winner", on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, blank=True, null=True, verbose_name="Buyer", on_delete=models.CASCADE)
    classifier_collection = models.ForeignKey(AuctionLotClassifier, blank=True, null=True,
                                              verbose_name="AuctionLotClassifier", on_delete=models.CASCADE)


class TradeResult(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    id_auction_message = models.TextField(blank=True, null=True, verbose_name="IdAuctionMessage")
    lot_table = models.ForeignKey(TradeResultLot, blank=True, null=True, verbose_name="LotTable",
                                  on_delete=models.CASCADE)


class Meeting(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    meeting_date = models.TextField(blank=True, null=True, verbose_name="MeetingDate")
    meeting_site = models.TextField(blank=True, null=True, verbose_name="MeetingSite")
    meeting_date_begin = models.TextField(blank=True, null=True, verbose_name="Meeting_date_begin")
    meeting_time_begin = models.TextField(blank=True, null=True, verbose_name="MeetingTimeBegin")
    registration_date = models.TextField(blank=True, null=True, verbose_name="RegistrationDate")
    registration_date_begin = models.TextField(blank=True, null=True, verbose_name="RegistrationDateBegin")
    registration_date_end = models.TextField(blank=True, null=True, verbose_name="RegistrationDateEnd")
    registration_site = models.TextField(blank=True, null=True, verbose_name="RegistrationSite")
    examination_date = models.TextField(blank=True, null=True, verbose_name="ExaminationDate")
    examination_site = models.TextField(blank=True, null=True, verbose_name="ExaminatationSite")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")
    fu_mail_address = models.TextField(blank=True, null=True, verbose_name="FuMailAddress")
    web_address = models.TextField(blank=True, null=True, verbose_name="WebAddress")
    meeting_form = models.TextField(blank=True, null=True, verbose_name="MeetingForm")


class MessageTypes(models.Model):
    arbitral_decree = models.ForeignKey(CourtDecision, null=True, blank=True, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, null=True, blank=True, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, null=True, blank=True, on_delete=models.CASCADE)
    meeting_result = models.ForeignKey(MeetingResult, null=True, blank=True, on_delete=models.CASCADE)
    trade_result = models.ForeignKey(TradeResult, null=True, blank=True, on_delete=models.CASCADE)
    other = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE, related_name="Other")
    appoint_administration = models.ForeignKey(AppointAdministration, null=True, blank=True, on_delete=models.CASCADE)
    change_administration = models.ForeignKey(ChangeAdministration, null=True, blank=True, on_delete=models.CASCADE)
    termination_administration = models.ForeignKey(TerminationAdministraion, blank=True, null=True,
                                                   on_delete=models.CASCADE)
    begin_executory_process = models.ForeignKey(BeginExecutoryProcess, blank=True, null=True, on_delete=models.CASCADE)
    transfer_assert_for_implementation = models.ForeignKey(TransferAssertsForImplementation, null=True, blank=True,
                                                           on_delete=models.CASCADE)
    annul = models.ForeignKey(Annul, null=True, blank=True, on_delete=models.CASCADE)
    property_inventory_result = models.ForeignKey(PropertyInventoryResult, blank=True, null=True,
                                                  on_delete=models.CASCADE)
    property_evaluation_report = models.ForeignKey(PropertyEvaluationReport, blank=True, null=True,
                                                   on_delete=models.CASCADE)
    assessment_report = models.ForeignKey(AssessmentReport, blank=True, null=True, on_delete=models.CASCADE)
    sale_contract_result = models.ForeignKey(SaleContractResult, blank=True, null=True, on_delete=models.CASCADE)
    sale_contract_result2 = models.ForeignKey(SaleContractResult2, blank=True, null=True, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, blank=True, null=True, on_delete=models.CASCADE)
    committee_result = models.ForeignKey(Other, blank=True, null=True, on_delete=models.CASCADE,
                                         related_name="committee_result_other")
    sale_order_pledged_property = models.ForeignKey(SaleOrderPledgedProperty, null=True, blank=True,
                                                    on_delete=models.CASCADE)
    receiving_creditor_demand = models.ForeignKey(ReceivingCreditorDemand, null=True, blank=True,
                                                  on_delete=models.CASCADE)
    demand_announcement = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                            related_name="demand_announcement_other")
    court_assert_acceptance = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                                related_name="court_assert_acceptance_other")
    financial_state_information = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                                    related_name="financial_state_information_other")
    bank_payment = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name="bank_payment_other")
    assert_returning = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                         related_name="assert_returning_other")
    court_acceptance_statement = models.ForeignKey(Other, null=True, blank=True, on_delete=models.CASCADE,
                                                   related_name="court_acceptance_statement_other")
    deliberate_bankruptcy = models.ForeignKey(DeliberateBankruptcy, null=True, blank=True, on_delete=models.CASCADE)
    intention_credit_org = models.ForeignKey(IntentionCreditOrg, null=True, blank=True, on_delete=models.CASCADE)
    liabilities_credit_org = models.ForeignKey(LiabilitiesCreditOrg, null=True, blank=True, on_delete=models.CASCADE)
    perfomance_credit_org = models.ForeignKey(PerformanceCreditOrg, null=True, blank=True, on_delete=models.CASCADE)
    buying_property = models.ForeignKey(BuyingProperty, null=True, blank=True, on_delete=models.CASCADE)
    declaration_person_damages = models.ForeignKey(DeclarationPersonDamages, null=True, blank=True,
                                                   on_delete=models.CASCADE)
    act_person_damages = models.ForeignKey(ActPersonDamages, null=True, blank=True, on_delete=models.CASCADE)
    act_review_person_damages = models.ForeignKey(ActReviewPersonDamages, null=True, blank=True,
                                                  on_delete=models.CASCADE)
    deal_invalid = models.ForeignKey(DealInvalid, blank=True, null=True, on_delete=models.CASCADE)
    act_deal_invalid = models.ForeignKey(ActDealInvalid, null=True, blank=True, on_delete=models.CASCADE)
    act_deal_invalid2 = models.ForeignKey(ActDealInvalid2, null=True, blank=True, on_delete=models.CASCADE)
    act_review_deal_invalid = models.ForeignKey(ActReviewDealInvalid, null=True, blank=True, on_delete=models.CASCADE)
    act_review_deal_invalid2 = models.ForeignKey(ActReviewDealInvalid2, null=True, blank=True, on_delete=models.CASCADE)
    declaration_person_subsidiary = models.ForeignKey(DeclarationPersonSubsidiary, null=True, blank=True,
                                                      on_delete=models.CASCADE)
    act_person_subsidiary = models.ForeignKey(ActPersonSubsidiary, null=True, blank=True, on_delete=models.CASCADE)
    act_person_subsidiary2 = models.ForeignKey(ActPersonSubsidiary2, null=True, blank=True, on_delete=models.CASCADE)
    act_review_person_subsidiary = models.ForeignKey(ActReviewPersonSubsidiary, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    act_review_person_subsidiary2 = models.ForeignKey(ActReviewPersonSubsidiary2, null=True, blank=True,
                                                      on_delete=models.CASCADE)
    meeting_worker = models.ForeignKey(MeetingWorker, null=True, blank=True, on_delete=models.CASCADE)
    meeting_worker_result = models.ForeignKey(MeetingWorkerResult, null=True, blank=True, on_delete=models.CASCADE)
    view_draft_restructuring_plan = models.ForeignKey(ViewDraftRestructuringPlan, null=True, blank=True,
                                                      on_delete=models.CASCADE)
    view_exec_restructuring_plan = models.ForeignKey(ViewExecRestructuringPlan, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    transfer_ownership_real_estate = models.ForeignKey(TransferOwnershipRealEstate, null=True, blank=True,
                                                       on_delete=models.CASCADE)
    cancel_auction_trade_result = models.ForeignKey(CancelAuctionTradeResult, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    cancel_deliberate_bankruptcy = models.ForeignKey(CancelDeliberateBankruptcy, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    change_auction = models.ForeignKey(ChangeAuction, null=True, blank=True, on_delete=models.CASCADE)
    change_deliberate_bankruptcy = models.ForeignKey(ChangeDeliberateBankruptcy, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    reducing_size_share_capital = models.ForeignKey(ReducingSizeShareCapital, null=True, blank=True,
                                                    on_delete=models.CASCADE)
    selection_purchaser_assets = models.ForeignKey(SelectionPurchaserAssets, blank=True, null=True,
                                                   on_delete=models.CASCADE)
    estimates_current_expenses = models.ForeignKey(EstimatesCurrentExpenses, blank=True, null=True,
                                                   on_delete=models.CASCADE)
    order_and_timing_calculations = models.ForeignKey(OrderAndTimingCalculations, blank=True, null=True,
                                                      on_delete=models.CASCADE)
    information_about_bankruptcy = models.ForeignKey(InformationAboutBankruptcy, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    estimates_and_unsold_assets = models.ForeignKey(EstimatesAndUnsoldAssets, null=True, blank=True,
                                                    on_delete=models.CASCADE)
    remaining_assets_and_right = models.ForeignKey(RemainingAssetsAndRight, null=True, blank=True,
                                                   on_delete=models.CASCADE)
    impending_transfer_assets = models.ForeignKey(ImpendingTransferAssets, null=True, blank=True,
                                                  on_delete=models.CASCADE)
    transfer_assets = models.ForeignKey(TransferAssets, blank=True, null=True, on_delete=models.CASCADE)
    transfer_insurance_portfolio = models.ForeignKey(TransferInsurancePortfolio, blank=True, null=True,
                                                     on_delete=models.CASCADE)
    bank_open_accout_debtor = models.ForeignKey(BankOpenAccountDebtor, null=True, blank=True, on_delete=models.CASCADE,
                                                related_name="bank_open_accout_debtor")
    procedure_granting_indemnity = models.ForeignKey(BankOpenAccountDebtor, null=True, blank=True,
                                                     on_delete=models.CASCADE)
    right_unsold_asset = models.ForeignKey(RightUnsoldAsset, null=True, blank=True, on_delete=models.CASCADE)
    transfer_responsibilities_fund = models.ForeignKey(TransferResponsibilitiesFund, null=True, blank=True,
                                                       on_delete=models.CASCADE)
    extension_administration = models.ForeignKey(ExtensionAdministration, null=True, on_delete=models.PROTECT,
                                                 blank=True)
    meeting_participants_building = models.ForeignKey(MeetingParticipantsBuilding, null=True, blank=True,
                                                      on_delete=models.PROTECT)
    meeting_part_build_result = models.ForeignKey(MeetingPartBuildResult, blank=True, null=True,
                                                  on_delete=models.CASCADE)
    part_build_monetaty_claim = models.ForeignKey(PartBuildMonetaryClaim, blank=True, null=True,
                                                  on_delete=models.CASCADE)
    start_settlement = models.ForeignKey(StartSettlement, null=True, blank=True, on_delete=models.CASCADE)
    process_inventory_debtor = models.ForeignKey(ProcessInventoryDebtor, blank=True, null=True,
                                                 on_delete=models.CASCADE)
    rebuttal = models.ForeignKey(Rebuttal, blank=True, null=True, on_delete=models.CASCADE)
    creditor_choice_right_subsidiary = models.ForeignKey(CreditorChoiceRightSubsidiary, blank=True, null=True,
                                                         on_delete=models.CASCADE)
    accession_declaration_subsidiary = models.ForeignKey(AccessionDeclarationSubsidiary, blank=True, null=True,
                                                         on_delete=models.CASCADE)
    disqualification_arbitration_manager = models.ForeignKey(DisqualificationArbitrationManager, blank=True, null=True,
                                                             on_delete=models.CASCADE)
    disqualification_arbitration_manager2 = models.ForeignKey(DisqualificationArbitrationManager2, blank=True,
                                                              null=True,
                                                              on_delete=models.CASCADE)
    change_estimates_current_expenses = models.ForeignKey(ChangeEstimatesCurrentExpenses, blank=True, null=True,
                                                          on_delete=models.CASCADE)
    return_of_application_on_extrajudicial_bankruptcy = models.ForeignKey(ReturnOfApplicationOnExtrajudicialBankruptcy,
                                                                          blank=True, null=True,
                                                                          on_delete=models.CASCADE)
    start_of_extrajudicial_bankruptcy = models.ForeignKey(StartOfExtrajudicialBankruptcy, blank=True, null=True,
                                                          on_delete=models.CASCADE)
    termination_of_extrajudicial_bankruptcy = models.ForeignKey(TerminationOfExtrajudicialBankruptcy, null=True,
                                                                blank=True, on_delete=models.CASCADE)
    completion_of_extrajudicial_bankruptcy = models.ForeignKey(CompletionOfExtrajudicialBankruptcy, null=True,
                                                               blank=True, on_delete=models.CASCADE)


class MessageInfo(models.Model):
    message_type = models.TextField(blank=True, null=True, verbose_name="Message Type")
    message_types = models.ForeignKey(MessageTypes, null=True,on_delete=models.CASCADE, blank=True)


class MessageData(models.Model):
    id_message_data = models.BigIntegerField(blank=True, null=True)
    number = models.CharField(max_length=30, null=True, blank=True, verbose_name="Номер сообщения")
    case_number = models.CharField(max_length=60, null=True, blank=True, verbose_name="Номер судебного дела")
    publish_date = models.DateTimeField(blank=True,null=True, verbose_name="Дата публикации")
    bankruptid = models.IntegerField(blank=True, null=True, verbose_name="BankruptId")
    message_guid = models.CharField(max_length=32, null=True,blank=True, verbose_name="MessageGUID")
    publisher_info = models.ForeignKey(PublisherInfo,null=True, blank=True, on_delete=models.CASCADE,
                                       verbose_name="PublisherInfo")
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Publsher")
    message_info = models.ForeignKey(MessageInfo, null=True, blank=True, on_delete=models.CASCADE, verbose_name="MessageInfo")
    bankrupt_info = models.ForeignKey(BankruptInfo, null=True, blank=True, on_delete=models.CASCADE,
                                      verbose_name="BankruptInfo")
    bankrupt = models.ForeignKey(Bankrupt, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Bankrupt")
    file_info_list = models.ForeignKey(FileInfoList, null=True, blank=True, on_delete=models.CASCADE,
                                       verbose_name='FileInfoList')
    message_url_list = models.ForeignKey(MessageURLList, null=True, blank=True, on_delete=models.CASCADE,
                                         verbose_name="MessageURLList")
