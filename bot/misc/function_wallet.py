from bot.data.config import client
import asyncio

# Создание чека
async def create_invoice(amount):
    try:
        invoice = await client.create_invoice(
            amount=amount,
            currency_type='fiat',
            fiat='USD',
            description='PanWin',
            allow_anonymous=False,
            expires_in=300
        )
        return invoice
    except Exception as e:
        print(f"Ошибка при создании чека: {e}")
        return None
    
# Получения статуса чека
async def check_invoice(invoice_id):
    try:
        # Получаем список всех инвойсов
        invoices = await client.get_invoices()
        
        # Ищем инвойс с заданным invoice_id
        for invoice in invoices:
            if invoice.invoice_id == invoice_id:
                return {
                    'invoice_id': invoice.invoice_id,
                    'status': invoice.status,
                    'comment': invoice.comment
                }
                
        return None  # Инвойс с таким ID не найден

    except Exception as e:
        print(f"Ошибка при получении статуса инвойса: {e}")
        return None
    
# Проверяем оплату чека
async def check_date_proverka(invoice_id):
    try:
        while True:
            invoice_status = await check_invoice(invoice_id)
            if invoice_status['status'] == 'paid':         
                return True
            
            elif invoice_status['status'] == 'expired':
                # Если закончилось время на активацию счета
                return False
            
            else:
                # Счет активен
                await asyncio.sleep(10)
    except Exception as e:
        print(f'Что то с проверкой оплаты.. {e}')