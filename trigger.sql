USE air
GO
CREATE TRIGGER tr_flight
ON ���мƻ����� AFTER INSERT
AS
DECLARE @flight_no varchar(50), @flight_type varchar(50), @plane_num varchar(50), @fly_no int
DECLARE @first_num int, @business_num int, @economy_num int
set @fly_no = (SELECT ���̺� from inserted)
set @flight_no = (SELECT ������ from inserted)
set @plane_num = (SELECT �ɻ���� FROM ���� WHERE ������ = @flight_no)
set @flight_type = (SELECT ���� FROM �ɻ��Ǽ� where �ɻ���� = @plane_num )
set @first_num = (SELECT ͷ�Ȳ����� FROM �ɻ��� WHERE ���� = @flight_type)
set @business_num = (SELECT ��������� FROM �ɻ��� WHERE ���� = @flight_type)
set @economy_num = (SELECT ���ò����� FROM �ɻ��� WHERE ���� = @flight_type)
IF @economy_num = 0
SET @economy_num = null
IF @business_num = 0
SET @business_num = null
IF @first_num = 0
SET @first_num = null
update ���мƻ�����
set [����գ���ʼ-���ʣ����λ] = @business_num, [����գ���ʼ-��ͣ��ʣ����λ] =@business_num, [����գ���ͣ-���ʣ����λ] = @business_num,
[���òգ���ʼ-���ʣ����λ] = @economy_num, [���òգ���ʼ-��ͣ��ʣ����λ]  = @economy_num, [���òգ���ͣ-���ʣ����λ]  = @economy_num,
[ͷ�Ȳգ���ʼ-���ʣ����λ]  = @first_num,[ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ]   = @first_num,[ͷ�Ȳգ���ͣ-���ʣ����λ]   = @first_num
where ���̺� = @fly_no