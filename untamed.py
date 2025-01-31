o
    Y��bQ� �                   @   s&  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlmZ d dlmZ d dl
mZ d dlZd dlmZ d dlZd dlZd dlmZ d dlmZmZmZ d dl	mZmZmZmZ d d	lm Z  d d
lm!Z!m"Z"m Z m#Z#m$Z$m%Z%m&Z& d dlZd dl'm(Z( d dl)m*Z* d dl)m+Z+ d dl,m-Z-m.Z.m/Z/m0Z0m1Z1m2Z2m3Z3m4Z4m5Z5m6Z6m7Z7m8Z8 d dl9m:Z:m;Z; d dl<m=Z= d dl)m+Z+m>Z> d dl'm?Z?m@Z@mAZA d dlBmCZC d dlDmEZEmFZFmGZGmHZHmIZImJZJmKZKmLZL d dlMmNZN dZOdZPdZQdZRdZdZSdZTdZUeVd� ze�Wd�ZXW n   eVe� d �� eVe� d!�� eY�  Y eZeXj[�d"k�r�e\e]eS� d#eXj[� d$e� ���Z^e^d%k�sUe^d&k�sUe^d'k�r�eVeS� d(�� ej_d)k�rme�`d*� e�`d+� n
e�`d,� e�`d-� e�`d.� e�`d/� eVeS� d0eXj[� �� e]d1� eY�  neVeS� d2�� e]d3� neVd4� eja�bd5��s�e�cd5� eja�bd6��s�edd6d7� eja�bd8��s�e�cd8� d9d:� Zed;d<� Zfd=d>� Zgd?d@� ZhdAdB� ZidCdD� ZjdEdF� ZkdGdH� ZldIdJ� ZmdKdL� ZndMdN� ZodOdP� Zpe�  ejqZrejsZtejuZvejwZxejyZTejzZ{ej|Z}etevexeTe{gZ~dQdR� ZdSdT� Z�dUdV� Z�dWdX� Z�dYdZ� Z�d[d\� Z�d]d^� Z�d_d`� Z�dadb� Z�dcdd� Z�dedf� Z�dgdh� Z�didj� Z�dkdl� Z�dmdn� Z�dodp� Z�dqdr� Z�dsdt� Z�dudv� Z�dwdx� Z�dydz� Z�d{d|� Z�d}d~� Z�dd�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�e��  dS )��    N)�track)�Client)�reader��sleep)�timezone)�MINYEAR�datetime�	timedelta)�Fore�Back�Style�init)�TelegramClient)�	functions�typesr   �
connection�sync�utils�errors)�LeaveChannelRequest)�ReportSpamRequest)�GetDialogsRequest)�InputPeerEmpty�UserStatusOffline�UserStatusRecently�UserStatusLastMonth�UserStatusLastWeek�PeerUser�PeerChannel�InputPeerChannel�InputPeerUser�ChannelParticipantsAdmins�UserStatusOnline�UserStatusEmpty)�GetContactsRequest�DeleteContactsRequest)�DeletePhotosRequest)r   �ImportChatInviteRequest)�GetFullChannelRequest�JoinChannelRequest�InviteToChannelRequest)�SessionPasswordNeededError)�UsernameInvalidError�ChannelInvalidError�PhoneNumberBannedError�YouBlockedUserError�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantError)�StringSessionz	@notoscami��� Z d038e172eb99839b69c39c3c25cd98cfi(� z[1;31mz[1;32mz[1;36mz[1,35mz                zKhttps://raw.githubusercontent.com/techzonebavan/untamed-v3/main/version.txtz& You are not connected to the internetz) Please connect to the internet and retryg      @z[~] Update available[Version z]. Download?[y/n]: �yZyes�Yz[i] Downloading updates...�ntzdel untamed.pyzdel setup.pyzrm untamed.pyzrm setup.pyzUcurl -l -O https://raw.githubusercontent.com/techzonebavan/untamed-v3/main/untamed.pyzScurl -l -O https://raw.githubusercontent.com/techzonebavan/untamed-v3/main/setup.pyz[*] Updated to version: zPress enter to exit...z[!] Update aborted.z Press enter to goto main menu...z               z
./sessions�	phone.csv�wz./Sessionssc                  C   s�   t �  tdd��L} dd� t�| �D �}d}|D ]3}t�|�}|d7 }ttjt	j
 d|� � � td|� �tt�}|�|� |td	�� |��  t�  qd
}W d   � n1 sWw   Y  t|rgtjt	j d nd� ttjt	j d � t�  d S )Nr9   �rc                 S   �   g | ]}|d  �qS �r   � ��.0�rowr>   r>   �"/storage/emulated/0/cre/untamed.py�
<listcomp>O   �    zlogin.<locals>.<listcomp>r   �   �Login �	sessions/�@The_Hacking_ZoneTzAll Number Login Done !�Error!zPress Enter to back)�banner�open�csvr   r   �parse_phone�printr   �BRIGHTr   �GREENr   �API_ID�HashID�startr*   �
disconnect�RESET�YELLOW�input)�f�str_list�po�pphone�phone�client�doner>   r>   rB   �loginI   s$   

�
r_   c               
   C   s�  t t�} tt�}g }d}tdd���}dd� t�|�D �}d}|D ]T}|d7 }t�|�}t	d|� �� t
d	|� �| |�}	|	��  |	�� sqzt	d
� t|�}
t|�}|�|� W q  typ   t	d� t|�}
t|�}|�|� Y q w t	�  q d}t	d� t	|ddi� t	d� tdddd��}tj|ddd�}|�|� W d   � n1 s�w   Y  W d   � n1 s�w   Y  dd� }dd� }|�  |�  t|r�d� d S d� d S )NFr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   g   rD   zBanFilter.<locals>.<listcomp>r   rE   rF   rG   zThis Phone Has Been RevokedZBanTzList Of Banned Numbers�sep�
zSaved In BanNumers.csv�BanNumbers.csvr:   �UTF-8��encoding�,�Z	delimiter�lineterminatorc               	   S   s^  g } g }g }g }g }t dd��}|D ]}| �|� qW d   � n1 s$w   Y  | D ]}t|��dd�}|�|� q+t d��+}t dd��}	|D ]}|	�|�dd�� qHW d   � n1 s^w   Y  W d   � n1 smw   Y  t dd��}	|	D ]}
|�|
� qzW d   � n1 s�w   Y  |D ]}t|��dd�}|�|� q�t|�}t|�}|�|�}|D ]}||vr�|�|� q�t d	dd
d��}tj|dd�}|�	|� W d   � n1 s�w   Y  t d	��0}t dd��}|D ]}t|��dd�}|�|� q�W d   � n	1 �s	w   Y  W d   � n	1 �sw   Y  t
�d� t
�d	d� td� d S )Nr9   r;   ra   � rb   zoutfile.csvr:   rf   �	unban.csvrc   rd   )rh   z(Done,All Banned Number Have Been Removed)rK   �append�str�replace�write�set�intersectionrL   �writer�	writerows�os�remove�renamerN   )Z
collectionZncZcollection1Znc1Zmaind�infile�line�xZmod_x�outfileZline1�iZmod_i�uniqueZunique1Zitd�	writeFilerq   Zlast�finalZline3r>   r>   rB   �
autoremove�   sd   ����� ��

����� 
zBanFilter.<locals>.autoremovec               	   S   s�   dd l } dd l}td��+}tdd��}|D ]}|�|�dd�� qW d   � n1 s+w   Y  W d   � n1 s:w   Y  |�d� |�dd� td� d S )Nr   r9   rj   r:   rf   ri   Zcomplete)rL   rs   rK   rn   rm   rt   ru   rN   )rL   rs   rv   ry   rw   r>   r>   rB   �dellst�   s   ��� 
zBanFilter.<locals>.dellst�Done!rI   )�intrQ   rl   rR   rK   rL   r   r   rM   rN   r   �connect�is_user_authorizedrk   r/   rq   rr   rW   )�api_id�api_hashZMadeByHackingZoner^   rX   rY   rZ   Zunparsed_phoner\   r]   �HackingZoneZNero_opr|   rq   r~   r   r>   r>   rB   �	BanFilter_   sV   


�	���)4r�   c               
   C   sV  t �  d} d}d}d}d}tdd��}}dd	� t�|�D �}d}|D ]f}t�|�}	|d
7 }ttjt	j
 dtj� dtjt	j � d|	� � � td|	� �tt�}
|
�|	� |
tjjdd�� |
�| d� t�d
� t|
�| ��}||v rzt|� |d
7 }ntd� |
��  t�  d}q!W d   � n1 s�w   Y  t|� d�� t|r�d� d S d� d S )NZSpamBotuT   Good news, no limits are currently applied to your account. You’re free as a bird!Zbirdr   Fr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �   rD   z"SpamBotChecker.<locals>.<listcomp>rE   rF   � rG   z@SpamBot��idz/startzyou are limitedTz - Accounts Are Usabler�   rI   )rJ   rK   rL   r   r   rM   rN   r   rO   r   rP   �	RESET_ALLrU   r   rQ   rR   rS   r   �contactsZUnblockRequest�send_message�timer   rl   �get_messagesrT   rW   )�bot�mr�   r;   r^   rX   rY   rZ   r[   r\   r]   �msgr>   r>   rB   �SpamBotChecker�   s<   
0


��r�   c                     s�  t �� } | �d� | d d �� }|�d�}| d d �� }ttjtj	 d|� � � t
d|� �tt�}|��  |�� rB|�|� �}d� g }|j|d	d
�}|t|��}|jj}� �fdd�}	tdddd��N}
tj|
ddd����g d�� z.t|�D ]'\}}t|d � d|� �dd� |d dkr�td� |js�|	||� � d � qzW n   td� Y W d   � n1 s�w   Y  |
��  td� d S )N�
config.inir�   �	FromGrouprf   �PhoneNumber�
Logging For rG   rE   T�Z
aggressivec              
      �r   |j r|j }nd}t|jt�r#��� ||j|j|j| j|jj	g� d S ��� ||j|j|j| jt
|j�jg� d S �Nri   ��username�
isinstance�statusr   �writerowr�   �access_hash�
first_name�title�
was_online�type�__name__��group�memberr�   ��countrq   r>   rB   rn   
  �   (,zScraper.<locals>.write�data.csvr:   rc   rd   ra   rg   ��sr. no.r�   �user idr�   �namer�   r�   �/���end�d   r   �   �c
There was a FloodWaitError, but check data.csv. More than 95%% of members should be already added.�
Users saved in the csv file.
)�configparser�ConfigParser�read�strip�splitrN   r   rO   r   rU   r   rQ   rR   r�   r�   �
get_entity�iter_participantsr)   �	full_chat�participants_countrK   rL   rq   r�   �	enumerater   r�   �close)�config�link1�linksr\   �cr�   �members�channel_full_info�contrn   rX   �indexr�   r>   r�   rB   �Scraper�   sF   



��
��r�   c                     s.  t j �� } | t jdd� }t�� }|�d� |d d �� }|�d�}|d d �� }tt	j
tj d|� � � td	|� �tt�}|��  |�� rO|�|� �}d� g }|j|d
d�}|t|��}	|	jj}
� �fdd�}tdddd���}tj|ddd����g d�� zrt|�D ]k\}}t|d � d|
� �dd� |d dkr�td� |js�t|jt t!f�r�|||� � d � q�t|jt"�r�|jj#}|j$| j$ko�|j%| j%ko�|j&| j&k}|j$|j$ko�|j%|j%ko�|j&|j&k}|s�|r�|||� � d � q�W n   td� Y W d   � n	1 �sw   Y  |�'�  td� d S )NrE   �Zdaysr�   r�   r�   rf   r�   r�   rG   Tr�   c              
      r�   r�   r�   r�   r�   r>   rB   rn   A  r�   zDailyFilter.<locals>.writer�   r:   rc   rd   ra   rg   r�   r�   r�   r�   r�   r   r�   r�   r�   )(r	   �nowr
   r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r�   r�   r)   r�   r�   rK   rL   rq   r�   r�   r   r�   r�   r�   r   r#   r   r�   �day�month�yearr�   )�today�	yesterdayr�   r�   r�   r\   r�   r�   r�   r�   r�   rn   rX   r�   r�   �dZ
today_userZyesterday_userr>   r�   rB   �DailyFilter'  sZ   





$$
��
��r�   c                     s(  t j �� } | t jdd� }t�� }|�d� |d d �� }|�d�}|d d �� }tt	j
tj d|� � � td	|� �tt�}|��  |�� rO|�|� �}d� g }|j|d
d�}|t|��}	|	jj}
� �fdd�}tdddd���}tj|ddd����g d�� zot|�D ]h\}}t|d � d|
� �dd� |d dkr�td� |js�t|jt t!t"f�r�|||� � d � q�t|jt#�r�|jj$}t%dd�D ]'}| t j|d� }|j&|j&ko�|j'|j'ko�|j(|j(k}|r�|||� � d � q�q�W n   td� Y W d   � n	1 �sw   Y  |�)�  td� d S )NrE   r�   r�   r�   r�   rf   r�   r�   rG   Tr�   c              
      r�   r�   r�   r�   r�   r>   rB   rn   �  r�   zWeeklyFilter.<locals>.writer�   r:   rc   rd   ra   rg   r�   r�   r�   r�   r�   r   r�   �   r�   r�   )*r	   r�   r
   r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r�   r�   r)   r�   r�   rK   rL   rq   r�   r�   r   r�   r�   r�   r   r#   r   r   r�   �ranger�   r�   r�   r�   �r�   r�   r�   r�   r�   r\   r�   r�   r�   r�   r�   rn   rX   r�   r�   r�   rz   �current_day�correct_userr>   r�   rB   �WeeklyFilterf  s\   





$
��
��r�   c                     sH  t �� } | �d� | d d �� }|�d�}| d d �� }ttjtj	 d|� � � t
d|� �tt�}|��  |�� rB|�|� �}d� g }|j|d	d
�}|t|��}|jj}� �fdd�}	tdddd��-}
tj|
ddd����g d�� |j|td�D ]}|js�|	||� � d � q|W d   � n1 s�w   Y  |
��  td� d S )Nr�   r�   r�   rf   r�   r�   rG   rE   Tr�   c              
      r�   r�   r�   r�   r�   r>   rB   rn   �  r�   zScrapAdmin.<locals>.writer�   r:   rc   rd   ra   rg   )r�   r�   r�   r�   z
name,groupr�   )�filterz
Admins saved in the csv file.
)r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r�   r�   r)   r�   r�   rK   rL   rq   r�   r"   r�   r�   )r�   r�   r�   r\   r�   r�   r�   r�   r�   rn   rX   r�   r>   r�   rB   �
ScrapAdmin�  s8   



���r�   c                     s*  t j �� } | t jdd� }t�� }|�d� |d d �� }|�d�}|d d �� }tt	j
tj d|� � � td	|� �tt�}|��  |�� rO|�|� �}d� g }|j|d
d�}|t|��}	|	jj}
� �fdd�}tdddd���}tj|ddd����g d�� zpt|�D ]i\}}t|d � d|
� �dd� |d dkr�td� |js�t|jt t!t"t#f�r�|||� � d � q�t|jt$�r�|jj%}t&dd�D ]'}| t j|d� }|j'|j'ko�|j(|j(ko�|j)|j)k}|r�|||� � d � q�q�W n   td� Y W d   � n	1 �sw   Y  |�*�  td� d S )NrE   r�   r�   r�   r�   rf   r�   r�   rG   Tr�   c              
      r�   r�   r�   r�   r�   r>   rB   rn   �  r�   zMonthlyFilter.<locals>.writer�   r:   rc   rd   ra   rg   r�   r�   r�   r�   r�   r   r�   �   r�   r�   )+r	   r�   r
   r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r�   r�   r)   r�   r�   rK   rL   rq   r�   r�   r   r�   r�   r�   r   r#   r   r   r   r�   r�   r�   r�   r�   r�   r�   r>   r�   rB   �MonthlyFilter�  s\   





$
��
��r�   c                     sd  t j �� } | t jdd� }t�� }|�d� |d d �� }|�d�}|d d �� }tt	j
tj d|� � � td	|� �tt�}|��  |�� rO|�|� �}d� g }|j|d
d�}|t|��}	|	jj}
� �fdd�}tdddd���}tj|ddd����g d�� z�g }g }t|�D ]o\}}t|d � d|
� �dd� |�|� |d dkr�td� |js�t|j t!t"t#t$f�r�|||� � d � |�|� q�t|j t%�r�|j j&}t'dd�D ]#}| t j|d� }|j(|j(ko�|j)|j)ko�|j*|j*k}|r�|�|� q�q�|D ]}||v�r|||� � d � q�W n   td� Y W d   � n	1 �s#w   Y  |�+�  td� d S )NrE   r�   r�   r�   r�   rf   r�   r�   rG   Tr�   c              
      r�   r�   r�   r�   r�   r>   rB   rn   -  r�   zNonActive.<locals>.writer�   r:   rc   rd   ra   rg   r�   r�   r�   r�   r�   r   r�   r�   r�   r�   ),r	   r�   r
   r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r�   r�   r)   r�   r�   rK   rL   rq   r�   r�   rk   r   r�   r�   r�   r   r#   r   r   r   r�   r�   r�   r�   r�   r�   )r�   r�   r�   r�   r�   r\   r�   r�   r�   r�   r�   rn   rX   Z	all_usersZactive_usersr�   r�   r�   rz   r�   r�   r>   r�   rB   �	NonActive  sl   





$
�

��
��r�   c                  C   s�  t jt jd� t�� } | �d� | d d �� }| d d �� }tdddd	��}t�	|�}d
d� |D �}W d   � n1 s>w   Y  tdddd	��}t�	|�}dd� |D �}W d   � n1 saw   Y  t
d|� �tt�}|��  |�� s�td|� d�� n�g }d }	d}
g }d}|dk�rVz�|�|�}|jdk�rt|j�}|j|dd�}g }g }d}g }|D ]}zt|j�|v r�|�|�t|j��� W q�   td� Y q�|��  |��  |jdd� |D ]}||= q�tddddd��}t�|�}|�|� W d   � n	1 �sw   Y  d}n
ttjtj d � d}W n7 t j!j"j#�y-   |t$|�� Y n% t%�yB   ttjtj& d � d}Y n   ttjtj d � d}Y |dks�t'� }dd� }d d!� }|�  |�  td"dd#d	��X}t�	|�}tddd#d	��;}tj|d$d%d&�}|�(g d'�� d}|D ]}|d(7 }|�(||d( |d) |d* |d+ |d, |d- f� �q�W d   � n	1 �s�w   Y  W d   � n	1 �s�w   Y  t)�*d.� t)�*d"� ttjtj+ d/ � ttjtj& d0 � ttjtj, d1 � t-�  d S )2N)�levelr�   r�   �ToGroupr�   r�   r;   zutf-8rd   c                 S   �   g | ]}|�qS r>   r>   �r@   rz   r>   r>   rB   rC   i  �    z(DeleteALreadyMembers.<locals>.<listcomp>c                 S   s   g | ]}t |d  ��qS )�   )rl   r�   r>   r>   rB   rC   m  s    rG   z
Login fail, for number z need Login first
��   r   �����Ti�  ��limitzError get user)�reverser:   ri   )re   �newlinez
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
c                  S   �   t � } tdddd��%}t�|�}|D ]}| �|� |D ]}|dkr&| �|� qqW d   � n1 s2w   Y  tdddd��}tj|dd	d
�}|�| � W d   � d S 1 sWw   Y  d S �Nr�   r;   rc   rd   ri   �1.csvr:   rf   ra   rg   ��listrK   rL   r   rk   rt   rq   rr   ��lines�readFiler   rA   �fieldr|   rq   r>   r>   rB   �main�  �    


����"�z"DeleteALreadyMembers.<locals>.mainc                  S   r�   �Nr�   r;   rc   rd   r�   �2.csvr:   rf   ra   rg   r�   r�   r>   r>   rB   �main1�  �    


����"�z#DeleteALreadyMembers.<locals>.main1r�   rc   rf   ra   rg   )r�   r�   r�   r�   r�   r�   ZStatusrE   r�   r�   �   �   �   r�   zAlready Member Deleted Done !zTask CompletedzPress Enter to exit).�loggingZbasicConfigZWARNINGr�   r�   r�   r�   rK   rL   r   r   rQ   rR   r�   r�   rN   r�   �	megagrouprl   r�   �get_participantsrk   r�   r�   rT   �sortrq   rr   r   rO   r   �RED�telethonr   Zrpcerrorlistr3   r*   �
ValueErrorrP   r�   r�   rs   rt   rU   rV   rW   )r�   �linkr\   rX   Zusers1�usersZuserlistr]   �chats�	last_date�
chunk_size�groups�nr�   Zgroup_id�all_participants�resultsZresults1r�   Zindex1�userrz   rn   r�   r�   r�   �source�rdrrq   rA   r>   r>   rB   �DeleteALreadyMembersY  s�   

�
�


�
��%
4����


r  c                  C   s�   d} t dd��O}dd� t�|�D �}d}|D ]8}t�|�}|d7 }ttjtj	 d|� � � t
d	|� �tt�}|�|� |tjj|�d
�d��}td� d} qW d   � n1 sYw   Y  t| rfd� d S d� d S )NFr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �  rD   zSetProfile.<locals>.<listcomp>r   rE   zChanging in rG   zuntamed.jpg)�filez"done! profile pic has been changedTr�   rI   )rK   rL   r   r   rM   rN   r   rO   r   rP   r   rQ   rR   rS   r   ZphotosZUploadProfilePhotoRequestZupload_filerW   )r^   rX   rY   rZ   r[   r\   r]   �resultr>   r>   rB   �
SetProfile�  s$   

���r  c                  C   s�   d} t dd��R}dd� t�|�D �}d}|D ];}t�|�}|d7 }ttjtj	 d|� � � t
d	|� �tt�}|�|� |t|�d
��� ttjtj d � d} qW d   � n1 s\w   Y  t| rid� d S d� d S )NFr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �  rD   z!DeleteProfile.<locals>.<listcomp>r   rE   zDeleting in rG   �mezProfile Pic DeletedTr�   rI   )rK   rL   r   r   rM   rN   r   rO   r   r  r   rQ   rR   rS   r'   Zget_profile_photosrP   rW   )r^   rX   rY   rZ   r[   r\   r]   r>   r>   rB   �DeleteProfile�  s    

��r  c                  C   s  t �d� tdt� dt� dt� d�� t�tjtj�} | �	d� tt
� dt� dt� t| �� d	 �� d
t
� dt� d�� tt
� dt� t �� � �� d}tj�td��}tt
� dt� |�|�� �� |�td��}tt
� dt� dt
� dt� |�|�� �� td� d S )N�clearra   u�  

                     
               ┏┳┳━┳┳━━┳━━┳━┳━┳━┳━━┓╋╋╋╋┏━━━┓
               ┃┃┃┃┃┣┓┏┫┏┓┃┃┃┃┃┳┻┓┓┃┏━┳━┫┏━┓┃
               ┃┃┃┃┃┃┃┃┃┣┫┃┃┃┃┃┻┳┻┛┃┗┓┃┏┻┛┏┛┃
               ┗━┻┻━┛┗┛┗┛┗┻┻━┻┻━┻━━┛╋┗━┛┏┓┗┓┃uj   
               ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┗━┛┃z

)z8.8.8.8�P   z	Your IP: r�   r   z             z	Version: Zv3zCurrent Directory: z%Y-%m-%d %H:%M:%S %Z%zZUTCzCurrent time in UTC: zAsia/KolkatazCurrent time in zAsia/Kolkata ztime zone: )rs   �systemrN   �cy�yer;   �socketZAF_INETZ
SOCK_DGRAMr�   �grr  rl   Zgetsockname�getcwdr	   r�   r   �strftimeZ
astimezone�be)�s�formatZnow_utcZnow_asiar>   r>   rB   rJ     s$   
��
�
6(rJ   c               	      s�   t �  tj�tj�tj�tj�tj�t�  g } g }g }tdd��}t	|�}t
|�}|D ]}|�t|d �� q+W d   � n1 sAw   Y  |�t�� d�� d�� tt|��� �� �� � ������fdd�����fdd	�� ��  d S )
Nr9   r;   r   �Total account: r�   c                      s6  t t�� d�� ���d } t t�� d�� ���}t t�� d�� ���}t t�� d�� ���}tdddd	��}tj|d
dd�}|�||| g� W d   � n1 sQw   Y  d}d}�| |� D �]�}|d7 }td|� �� t�|�}	tt	j
tj dt	j� dt	j
tj � d|	� � � td|	� �tt�}
|
��  |
�� s�t�� d�� �� |
�|	� |
�|	td�� d}g }t|dd	��;}tj|d
dd�}t|d � |D ]#}i }|d |d< |d |d< t |d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �s&w   Y  t |�}|| }tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sZw   Y  t |�}|| }tdddd	��}tj|d
dd�}|�||g� W d   � n	1 �s�w   Y  d}|D ]y}t |�t |d �k�r
t |d �t |�k�r
z1|d7 }|d dk�r�t�� d�� �� W �q�|
tjj|d |d td�dd d!�� |� d"�}W n* tj�y� } z
|j j!}W Y d }~nd }~w   t"�#�  t�� d#�� �� Y �q�t|� �q�|d7 }q`t$�%d� � �  d S )$N�From Account No : rE   �Upto Account No : zFrom where you want to start : z3How many contacts you want to add in one Account : �
memory.csvr:   rc   rd   rf   ra   rg   r   �Index : rF   r�   rG   �some thing has changed�Enter the code: r�   �srnor�   r�   r�   r�   r�   r;   ri   �	Just Nextr�   ZgdfT)r�   r�   �	last_namer\   Zadd_phone_privacy_exception� - done�Unexpected Error)&r�   rW   rK   rL   rq   r�   rN   r   rM   r   rO   r   rP   r�   rU   r   rQ   rR   r�   r�   �send_code_request�sign_inr   �nextrk   r�   r   r�   ZAddContactRequestrl   r   �RPCError�	__class__r�   �	traceback�	print_excrs   rt   ) �From�Upto�rex�hacksr  rq   �a�indexx�xdr\   r]   �
input_filer  rX   �rowsrA   r  �hash_obj�
csv_reader�list_of_rows�
row_number�
col_number�numnext�	startfrom�	nextstart�numend�endto�nextend�df�itr�   �e)�again�blr  r  r[   r;   r  r>   rB   �autosF  s�   �
0

���	��,���


z"AutoaddContactPhone.<locals>.autosc                     s.   t �� d�� ��} | dkr� �  d S t�  d S )NzRDone!
Choose From Below:

1 - Repeat The Script
OR Just Hit Enter To Quit

Enter: �1)rW   �quit)�stat)rP  r  r;   r>   rB   rN  �  s   

z"AutoaddContactPhone.<locals>.again)r   r   �LIGHTRED_EXrP   rU   �BLUErV   rJ   rK   r   �tuplerk   r�   rN   rl   �len)r�   r�   r\   �	delta_objrA  �list_of_phone�phone_r>   )rN  rP  rO  r  r  r[   r;   r  rB   �AutoaddContactPhone*  s,   ��(i
r[  c                  C   s�  t jdd� ttjtj d � t� } t| � d�d��}dd� t	�
|�D �aW d   � n1 s0w   Y  tdttt�� � ttd	��d
 }ttd��}d}dat||� D ]y}|d
7 }td|� �� t�|�}td|� �� td|� �tt�}|�|� |tdd��}d}	|jD ]E}
|	d
7 }	z|t|
gd�� ttjtj |	� d|
j� d� � W q� tjy� } z|jj}t|	� d|
j� d|� �� W Y d }~q�d }~ww qWd S )NT)Z	autoresetzEnter Accounts List : z.csvr;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �  rD   z!DeleteContact.<locals>.<listcomp>r$  r%  rE   r&  r   r(  rF   rG   ��hashr�   � - z	 - DELETE)�coloramar   rN   r   rO   r   rP   rW   rK   rL   r   �phlistrl   rW  r�   �HackingZonepror   rM   r   rQ   rR   rS   r%   r  r&   r�   r   r3  r4  r�   )ZphonecsvrX   � HackingZone_ne_script_banaya_hai�5telegram_script_banyane_ke_liye_HackingZone_ko_dm_kror<  ZHackingZoneonytr\   r]   r�   ZrexaddZrexoprM  �error>   r>   rB   �DeleteContact�  sB   �


&����re  c                   C   s�  t �� } | �d� | d d }| d d }| d d }| d d }| d d }tdd	��}d
d� t�|�D �}W d   � n1 sAw   Y  tdtt|�� � tt	j
tj d � t� }tt	j
tj d � tt� �}	tt	j
tj d � tt� �}
|dkr�t|�}|}n
|dkr�t|�}|}t|�}t|�d }t|�}d}da|||� D �]}|d7 }t�|�}td|� �� td|� �tt�}|�|� td|� �� z	|�t|��}W n3 t�y   |dkr�|t|�� |�t|��}n|dk�r
|t|�� t�d� |�t|��}Y nw |t|d��}t|jj �atdt� �� t|k�r4td|� d�� t�  t!�  |t"dd��}|j#}t|�}td|� �� d}d}||k �r�dd� |d |	� D �}zDt�|
� |t$j%j&||d�� ||	7 }t'dd �D ]}z||= W �qv t(�y� } zW Y d }~�qvd }~ww tt	j
tj d!|� � � W n t)j*�y� } z|j+j,}tt|�� W Y d }~n
d }~ww ||k �sRq�d S )"Nr�   r�   r�   �GroupID�	EnterStop�StartingAccount�
EndAccountr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �  rD   zBulkAdder.<locals>.<listcomp>r$  �1Enter Y if group has private link else N (Y/N) : z.In A Batch How many Members You Want To Add : �*Enter Delay Time Per Request 0 For None : r7   �NrE   r   rF   rG   r(  r�   ��channel�	Members: �The Goal Of � Has Been Completedr\  zTotal : c                 S   r�   r>   r>   )r@   Zdeltar>   r>   rB   rC   $  r�   �rn  r  �
   zBATCH: )-r�   r�   r�   rK   rL   r   rN   rl   rW  r   rO   r   rP   rW   r�   ZLegenddev_is_main_developerr   rM   r   rQ   rR   rS   r�   r   r  r(   �get_input_entityr*   r�   r   r)   r�   r�   rR  r%   r  r   �channelsr+   r�   �	Exceptionr   r3  r4  r�   ) r�   �	grouplink�groupid�stopnum�stacno�endacnorX   r`  �prchkZLegenddevismain�HackingZone_devr�   �prlink�stopZ
start_fromZuptor<  Zpythondeveloperr\   r]   rn  �channelinfor�   �user_to_addZcountconZ
batchcountZlolZsemenrz   �DrM  rd  r>   r>   rB   �	BulkAdder�  s�   
�





��	


�����
���r�  c                  C   s  t �� } | �d� | d d }| d d }| d d }| d d }| d d }tdd	��}d
d� t�|�D �}W d   � n1 sAw   Y  tdtt|�� � tt	j
tj d � t� }tt	j
tj d � tt� �}	|dkrwt|�}
|}n
|dkr�t|�}
|}t|�}t|�d }t|�}d}da|||� D ]�}|d7 }td|� �� t�|�}td|� �� td|� �tt�}|�|� z	|�t|
��}W n1 ty�   |dkr�|t|�� |�t|
��}n|dkr�|t|�� t�d� |�t|
��}Y nw |t|d��}t|jj �atdt� �� t|k�r"td|� d�� t�  t!�  |t"dd��}d}|j#D ]T}|d7 }z"|t$|
|gd�� tt	j
tj |� d|j%� d� � t�|	� W �q. t&j'�y� } z|j(j)}tt	j
tj* |� d|j%� d|� � � W Y d }~�q.d }~ww q�d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   E  rD   zSingleAdder.<locals>.<listcomp>r$  rj  rk  r7   rl  rE   r   r(  rF   rG   r�   rm  ro  rp  rq  r\  rr  r^  z - DONE)+r�   r�   r�   rK   rL   r   rN   rl   rW  r   rO   r   rP   rW   r�   ra  r   rM   r   rQ   rR   rS   r�   r   r  r(   rt  r*   r�   r   r)   r�   r�   rR  r%   r  r+   r�   r   r3  r4  r�   r  )r�   rw  rx  ry  rz  r{  rX   r`  r|  r}  r�   r~  r  rb  rc  r<  Zdeltaxdr\   r]   rn  r�  r�   ZdeltaaddZdeltaoprM  rd  r>   r>   rB   �SingleAdder9  s�   
�



��	

"&����r�  c                     s  t � } dd� }tdddd��}tj|ddd	�}|�| � W d   � n1 s&w   Y  d
d� }|�  |�  tdddd��V}t�|�}tdddd��:}tj|ddd	�}|�g d�� d}|D ]}	|d7 }|�||	d |	d |	d |	d |	d |	d f� q]W d   � n1 s�w   Y  W d   � n1 s�w   Y  t�d� t�d� t	�  t
tjtj d � tt� �}
tdd��}t|�}t |�}|
}d}||d  |d  }W d   � n1 s�w   Y  t�t� |�t�� }|�d� |d d �� ���fdd�}|�  d S )Nc                  S   st   t � } tdddd��&}t�|�}|D ]}| �|� |D ]}|dkr&| �|� qqW d   � d S 1 s3w   Y  d S )Nr�   r;   rc   rd   ri   )r�   rK   rL   r   rk   rt   )r�   r�   r   rA   r�   r>   r>   rB   r�   �  s   


���"�zAdder.<locals>.mainr�   r:   rc   rd   rf   ra   rg   c                  S   r�   r�   r�   r�   r>   r>   rB   r�   �  r�   zAdder.<locals>.main1r�   r;   r�   r�   r   rE   r�   r�   r�   r�   r�   �'Which Account You Want To Use?

Enter: r9   r�   r�   r�   c                     s�  �} t ���}td|� ��� �}|��  |�� sHz|�|� |�|td�� td� |�|� W n t	yG   td�}td� |j|d� Y nw d}g }t
|dd��;}tj|d	d
d�}t|d � |D ]#}i }	|d |	d< |d |	d< t|d �|	d< |d |	d< |�|	� qbW d   � n1 s�w   Y  ttd��}
ttd��}|D �]*}	t|
�t|	d �k�r�t|	d �t|�k�r�z1d}|	d dkr�td� W q�|t| |	d g�� tjtj d }ttjtj d � t�d� W n� t�y   tjtj d }t�d� Y n� t�y   d}Y nx t�y2 } zd}ttjtj d � t�d� W Y d }~nYd }~w t�yO } z|t| �� t�d� W Y d }~q�d }~w tj�yf } z
|j j!}W Y d }~n%d }~w t"�yz } z|}W Y d }~nd }~w   t#�$�  td� Y q�|�%| �}|t&|d ��}t|j'j(�}ttjtj) d!|� tj*� d"tjtj+ � d#|	d � d$|� �	 � q�t|	d �t|�k�r�td%� t�  t,�  q�d S )&NrG   �Enter code: ri   �Enter password: ��passwordr�   rc   rd   rf   ra   rg   r   r+  rE   r�   r�   r�   r�   r�   zStart From = z	End To = r}  zno username, moving to nextZDONEzMoving To NextZPrivacyRestrictedErrorZALREADYr1   z(Script Are In Progress So Please Wait...r�   r/  rm  zGroup Members r�   z>> z >> zMembers Added Successfully!)-r   rM   r   r�   r�   r0  r1  rW   rN   r,   rK   rL   r   r2  r�   rk   r+   r   rO   r   rP   rV   r�   r   r2   r  r4   r1   r3   r*   r   r3  r4  r�   rv  r5  r6  r�   r)   r�   r�   rU   r�   �CYAN�exit)Zchannel_usernamer\   r]   r�  r>  r  rX   r?  rA   r  rF  rI  r�   �g�cwferM  r�   Zchannel_connectr�   Zcountt�r�   r�   r[   Zto_groupr>   rB   rP  �  s�   

�
��
,�
���
@��zAdder.<locals>.autos)r�   rK   rL   rq   rr   r   r�   rs   rt   r   rN   r   rO   r   rV   r�   rW   rQ   rR   r�   r�   r�   )r�   r�   r|   rq   r�   r  r  rX   rz   rA   ZHackingZone_devinput�read_objrA  rB  rC  rD  �valuer�   rP  r>   r�  rB   �Adder  sT   �
2����


�

Yr�  c            	         s�   t d� t tjtj d � tt� �} tdd��}t|�}t	|�}| }d}||d  |d  }W d   � n1 s9w   Y  t
�t� |�t�� }|�d� |d d �� ���fd	d
�}|�  d S )Nz"choose accout that are not limitedr�  r9   r;   rE   r�   r�   r�   c                     s�  t ���} td| � ��� �}|��  |�� sFz|�| � |�| td�� td� |�| � W n t	yE   td�}td� |j|d� Y nw �}td� g }|j
|dd�}td	� td
ddd��J}tj|ddd�}|�g d�� |D ]0}|jr{|j}nd}|jr�|j}	nd}	|jr�|j}
nd}
|	d |
 �� }|�||j|j|g� qrW d   � n1 s�w   Y  tdt� �� |�� j}td|� dt� �� d}d}ttdt� ���}g }td
dd��=}tj|ddd�}t|d � |D ]%}i }|d |d< t|d �|d< t|d �|d< |d |d< |�|� q�W d   � n	1 �sw   Y  d}ttd t� ���}|D ]�}|dk�rH|d dk�r@�q0|�|d �}n|dk�rWt|d |d �}ntd!t� �� |��  t �!�  z!td"|d � |�"||�#|d �� td#�#|�� t$�%|� W �q0 t&�y�   td$� td#�#|�� t$�%|� Y �q0 t'�y� } ztd%|� td&� td#�#|�� t$�%|� W Y d }~�q0d }~ww |��  td'� td(� d S ))NrG   r�  ri   r�  r�  zFetching Members...Fr�   zSaving In file...z	msend.csvr:   rc   rd   rf   ra   rg   )r�   r�   zaccess hashr�   r�   zMembers scraped successfully.zMessage was sending throuh �(   �   z'Enter sleep time duration in messages :r   r�   rE   r�   r�   r�   r�   r�   zsend your messsagezInvalid Mode. Exiting.zSending Message to:�Waiting {} seconds�\Getting Flood Error from telegram. Script is stopping now. Please try again after some time.zError:zTrying to continue...z Done. Message sent to all users.z"
 Press enter to goto main menu...)(r   rM   r   r�   r�   r0  r1  rW   rN   r,   r  rK   rL   rq   r�   r�   r�   r-  r�   r�   r�   �lg�get_mer  r�   r   r2  rk   rl   rt  r!   rT   �sysr�  r�   r#  r�   r   r1   rv  )r\   r]   r�  �target_groupr  rX   rq   r  r�   r�   r-  r�   �acc_name�SLEEP_TIME_2ZSLEEP_TIME_1Z
SLEEP_TIMEr  r?  rA   �mode�messageZreceiverrM  r�  r>   rB   �	sedmrunalC  s�   

���

��



��z messagesender.<locals>.sedmrunal)rN   r   rO   r   rV   r�   rW   rK   r   r�   rQ   rR   r�   r�   r�   )	ZLegend_devinputr�  rA  rB  rC  rD  r�  r�   r�  r>   r�  rB   �messagesender-  s$   
�

]r�  c                  C   st  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]�}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r|�� j}z|td�� |�t|� td|� |� |� d�� |d7 }W n t �y } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s3w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   � Total accounts: z% Enter number of accounts to Report: z Send Message For Report rE   z -- Sending Reports from � account(s) --r(  rG   �User: � -- �Starting session... rH   zReport Done From: z  To Notoscam-- ra   �session endedzAll reports done sucesfully)!r   rU   rU  r  �WHITEr�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   r*   r�   �scamrv  )r  r�  r;   r:   r  r  r  �colorsr�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   �number_of_accs�choice�
sleep_time�send_status�approx_members_countr�   �accr�   r�  rM  r>   r>   rB   �ScamTag�  sl   
 



��
�$�r�  c               
   C   s�  t �� } | �d� | d d �� }|�d�}| d d �� }ttjtj	 d|� � � t
d|� �tt�}|��  |�� sU|�|� t�d� t�  |�|ttd	 t �� g }td
dd��=}tj|ddd�}t|d � |D ]%}i }	|d |	d< t|d �|	d< t|d �|	d< |d |	d< |�|	� qmW d   � n1 s�w   Y  g }
d }d}g }|t|dt� |dd��}|
�|j � |
D ]}z|j!dkr�|�|� W q�   Y q�ttd t" � d}|D ]}tt#|�d |j$ � |d7 }q�ttd t �}|t|� }t%|j&|j'�}tttd t" ��}d}|D ]�}	|d7 }|d dk�r$t(d � zLtd!�)|	d �� |dk�rE|	d d"k�r=W �q|�*|	d �}n|dk�rTt+|	d |	d �}nt,�-d#� |t.||g�� td$� t/�(t0�1dd%�� W �q t2�y�   td&� td'�)t3�� Y �q t4�y�   td&� t/�(t3� Y �q t5�y�   td(� td)� t/�(t0�1dd%�� Y �q   t6�7�  td*� Y �qd S )+Nr�   r�   r�   rf   r�   r�   rG   r  z[+] Enter the code: r�   rc   rd   ra   rg   rE   r�   r�   r�   r�   r�   r�   r�   r�   r   �Zoffset_dateZ	offset_idZoffset_peerr�   r]  TzChoose a group to add members:z- zEnter a Number: z.Enter 1 to add by username or 2 to add by ID: r  �<   z	Adding {}ri   z(Invalid Mode Selected. Please Try Again.zWaiting for 60-180 Seconds...r�   r�  r�  zBThe user's privacy settings do not allow you to do this. Skipping.zWaiting for 5 Seconds...r/  )8r�   r�   r�   r�   r�   rN   r   rO   r   rU   r   rQ   rR   r�   r�   r0  rs   r  rJ   r1  rW   r  �rerK   rL   r   r2  r�   rk   r   r   �extendr  r   r  rl   r�   r    r�   r�   r   r#  rt  r!   r�  r�  r+   r�   �randomZ	randranger1   r�  ZFloodWaitErrorr2   r5  r6  )r�   r�   r�   r\   r]   r  rX   r?  rA   r  r  r	  r
  r  r  �chatrz   r�   �g_indexr�  Ztarget_group_entityr�  r  r�  r>   r>   rB   �SingleJoinedAdder�  s�   




���

�



�r�  c                     sv  t � } dd� }dd� }|�  |�  tdddd��V}t�|�}td	d
dd��:}tj|ddd�}|�g d�� d}|D ]}|d7 }|�||d |d |d |d |d |d f� q9W d   � n1 sbw   Y  W d   � n1 sqw   Y  t�d� t�d� t�  t	j
�t	j�t	j�t	j}	t	j�	t�� }
|
�d� |
d d �|
d d �|
d d �|
d d �|
d d � g }tdd�� }t|�}t|�}|D ]}|�t|d �� q�|�W d   � n1 s�w   Y  t�� d�� d �� tt|��� �� �� � ���������	f
d!d"�}� ���������	f
d#d$�}tt|	� d%�� ���}|d&k�r/|�  d S |d'k�r9|�  d S d S )(Nc                  S   r�   r�   r�   r�   r>   r>   rB   r�   F  r�   zUsernameAdder.<locals>.mainc                  S   r�   r�   r�   r�   r>   r>   rB   r�   Z  r�   zUsernameAdder.<locals>.main1r�   r;   rc   rd   r�   r:   rf   ra   rg   r�   r   rE   r�   r�   r�   r�   r�   r�   r�   r�   r�   rf  rg  rh  ri  r9   r$  r�   c            )         s�  t tjtj d � tt� �} d}t��}t��}t��d }t� �}td�}td�d }t��}tdddd��}	t	j
|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]�}|d7 }t d|� �� t�|�}t d|� �� td|� �tt�}|��  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��;}t	j|d	d
d�}t|d � |D ]#}i }|d |d< |d |d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sw   Y  t|�}|| }tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sLw   Y  t|�}|| } tdddd��}!t	j
|!d	d
d�}
|
�|| g� W d   � n	1 �s{w   Y  |t|�� t�d� |�t|��}"|t|"d��}#t|#jj �}$t d|$� �� |$|k�r�t d|� d�� t�  t!�  d}%|D ]�}t|�t|d �k�rZt|d �t|�k�rZz2|%d7 }%|d dk�r�t �� d�� �� W �q�|t"j#�$||d g�� t |%� d �� t�| � W �q� t%�y& }& z|t|�� t�d� W Y d }&~&�q�d }&~&w t&j'�yG }' z|'j(j)}(t |%� d!|(� �� W Y d }'~'�q�d }'~'w   t*�+�  t �	� d"�� �� Y �q��q�|d7 }qct,�-d� d S )#Nrk  r�   rE   �2   r'  r:   rc   rd   rf   ra   rg   r   r(  rF   rG   r)  r*  r+  r�   r�   r�   r�   r�   r;   r�   rm  ro  rp  rq  ri   r,  r.  r^  r/  ).rN   r   rO   r   rP   r�   rW   rl   rK   rL   rq   r�   r   rM   r   rQ   rR   r�   r�   r0  r1  r   r2  rk   r�   r*   r�   r   rt  r   r)   r�   r�   rR  r   ru  r+   r3   r   r3  r4  r�   r5  r6  rs   rt   ))r}  r�   �rexlinkr�   r7  r8  r9  r:  r  r  rq   r;  r<  r=  r\   r]   r>  r  rX   r?  rA   r  r@  rA  rB  rC  rD  rE  rF  rG  rH  rI  rJ  rK  rn  r�  �rexprodeltanoobrL  r�  rM  r�   �
r{  r  rx  rw  r  r[   r;   rz  ry  r  r>   rB   rP  �  s�   
�


���	��

,
� ��
zUsernameAdder.<locals>.autosc            *         s�  t tjtj d � tt� �} d}t��}t��}t��d }t� �}td�}td�d }t��}tdddd��}	t	j
|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]}|d7 }t d|� �� t�|�}t d|� �� td|� �tt�}|��  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��C}t	j|d	d
d�}t|d � |D ]+}i }|d |d< |d |d< t|d �|d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �s w   Y  t|�}|| }tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sTw   Y  t|�}|| } tdddd��}!t	j
|!d	d
d�}
|
�|| g� W d   � n	1 �s�w   Y  |tjj|d��}"t�d� |�t|��}#|t |#d��}$t|$j!j"�}%t d|%� �� |%|k�r�t d|� d�� t�  t#�  d}&|D ]�}t|�t|d �k�rlt|d �t|�k�rlt d|%� �� z2|&d7 }&|d d k�r�t �� d!�� �� W �q�|tj$�%||d g�� t |&� d"�� t�| � W �q� t&�y8 }' z|t|�� t�d� W Y d }'~'�q�d }'~'w t'j(�yY }( z|(j)j*})t |&� d#|)� �� W Y d }(~(�q�d }(~(w   t+�,�  t �	� d$�� �� Y �qȐq�|d7 }qct-�.d� d S )%Nrk  r�   rE   r�  r'  r:   rc   rd   rf   ra   rg   r   r(  rF   rG   r)  r*  r+  r�   r�   r�   r�   r�   r�   r;   r\  r�   rm  ro  rp  rq  ri   r,  r.  r^  r/  )/rN   r   rO   r   rP   r�   rW   rl   rK   rL   rq   r�   r   rM   r   rQ   rR   r�   r�   r0  r1  r   r2  rk   r�   r   �messagesr(   r�   r   rt  r   r)   r�   r�   rR  ru  r+   r3   r   r3  r4  r�   r5  r6  rs   rt   )*r}  r�   r�  r�   r7  r8  r9  r:  r  r  rq   r;  r<  r=  r\   r]   r>  r  rX   r?  rA   r  r@  rA  rB  rC  rD  rE  rF  rG  rH  rI  rJ  rK  r  rn  r�  r�  rL  r�  rM  r�   r�  r>   rB   �private  s�   
�


���	���

,
� ��
zUsernameAdder.<locals>.private�%Press Y if group is private else N : r7   rl  )r�   rK   rL   r   rq   r�   rs   rt   r   r   rT  rP   rU   rU  rV   r�   r�   r�   rV  rk   r�   rN   rl   rW  rW   )r�   r�   r�   r  r  rX   rq   rz   rA   rO  r�   r\   rX  rA  rY  rZ  rP  r�  �	rexchooser>   r�  rB   �UsernameAdderA  sd   
2����


�(yy



�r�  c               	      sn  t �  tj�tj} tj�tj}tj�t�� }|�	d� |d d �|d d �|d d �|d d �|d d � g }t
dd	��}t|�}t|�}|D ]}|�t|d
 �� qKW d   � n1 saw   Y  |�t| � d�� d�� tt|��� �� �� � ��������f	dd�}� ��������f	dd�}	tt|� d�� ���}
|
dkr�|	�  d S |
dkr�|�  d S d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r$  r�   c            *         s�  t tjtj d � tt� �} d}t��}t��}t��d }t� �}td�}td�d }t��}tdddd��}	t	j
|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]�}|d7 }t d|� �� t�|�}t d|� �� td|� �tt�}|��  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��C}t	j|d	d
d�}t|d � |D ]+}i }|d |d< |d |d< t|d �|d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �s w   Y  t|�}|| }tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sTw   Y  t|�}|| } tdddd��}!t	j
|!d	d
d�}
|
�|| g� W d   � n	1 �s�w   Y  |t|�� t�d� |�t|��}"|t|"d��}#t|#jj �}$t d|$� �� |$|k�r�t d|� d�� t�  t!�  d}%|D ]�}t|�t|d �k�rTt|d �t|�k�rTz$|%d7 }%t"|d |d �}&|t#||&g�� t |%� d �� t�| � W �q� t$�y  }' z|t|�� t�d� W Y d }'~'�q�d }'~'w t%j&�yA }( z|(j'j(})t |%� d!|)� �� W Y d }(~(�q�d }(~(w   t)�*�  t �� d"�� �� Y �qŐq�|d7 }qct+�,d� d S �#Nrk  r�   rE   r�  r'  r:   rc   rd   rf   ra   rg   r   r(  rF   rG   r)  r*  r+  r�   r�   r�   r�   r�   r�   r�   r;   r�   rm  ro  rp  rq  r.  r^  r/  )-rN   r   rO   r   rP   r�   rW   rl   rK   rL   rq   r�   r   rM   r   rQ   rR   r�   r�   r0  r1  r   r2  rk   r�   r*   r�   r   rt  r   r)   r�   r�   rR  r!   r+   r3   r   r3  r4  r�   r5  r6  rs   rt   �*r}  r�   r�  r�   r7  r8  r9  r:  r  r  rq   r;  r<  r=  r\   r]   r>  r  rX   r?  rA   r  r@  rA  rB  rC  rD  rE  rF  rG  rH  rI  rJ  rK  rn  r�  r�  rL  r�  r�  rM  r�   �	r{  rx  rw  r  r[   r;   rz  ry  r  r>   rB   rP  �  s�   
�


���	��

,
� ��
zAdderForPhone.<locals>.autosc            *         s�  t tjtj d � tt� �} d}t��}t��}t��d }t� �}td�}td�d }t��}tdddd��}	t	j
|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]�}|d7 }t d|� �� t�|�}t d|� �� td|� �tt�}|��  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��C}t	j|d	d
d�}t|d � |D ]+}i }|d |d< |d |d< t|d �|d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �s w   Y  t|�}|| }tdd��}t|�}t|�}d}d}||d  |d  }W d   � n	1 �sTw   Y  t|�}|| } tdddd��}!t	j
|!d	d
d�}
|
�|| g� W d   � n	1 �s�w   Y  |t|�� t�d� |�t|��}"|t|"d��}#t|#jj �}$t d|$� �� |$|k�r�t d|� d�� t�  t!�  d}%|D ]�}t|�t|d �k�rGt|d �t|�k�rGt d|$� �� z|%d7 }%t"|d |d �}&W �q� t&�y }' z|t|�� t�d� W Y d }'~'�q�d }'~'w t'j(�y4 }( z|(j)j*})t |%� d!|)� �� W Y d }(~(�q�d }(~(w   t+�,�  t �� d"�� �� Y �qŐq�|d7 }qct-�.d� d S r�  )/rN   r   rO   r   rP   r�   rW   rl   rK   rL   rq   r�   r   rM   r   rQ   rR   r�   r�   r0  r1  r   r2  rk   r�   r(   r�   r   rt  r   r)   r�   r�   rR  r!   r   ru  r+   r3   r   r3  r4  r�   r5  r6  rs   rt   r�  r�  r>   rB   r�  *  s�   
�


���	��

,
� ��
zAdderForPhone.<locals>.privater�  r7   rl  )r   r   rT  rP   rU   rU  rV   r�   r�   r�   rK   r   rV  rk   r�   rN   rl   rW  rW   )r  rO  r�   r\   rX  rA  rY  rZ  rP  r�  r�  r>   r�  rB   �AdderForPhone�  s>   
��(vx

�r�  c                  C   s�   t dddd��} tj| ddd�}|�g d�� W d   � n1 s!w   Y  ttd	��d
 }d}||krItj dtjd� |d
 }t�	d� ||ks4t�	d� t
�d� d S )Nr'  r:   rc   rd   rf   ra   rg   )rE   rE   r�  z*How many accounts do you want to run ? => rE   r   zpython v1-1.py)Zcreationflagsr�   rs  )rK   rL   rq   r�   r�   rW   �
subprocessZCREATE_NEW_CONSOLEr�   r   rs   rt   )r  rq   r;  rx   r>   r>   rB   �MultipleAdder�  s   �
�
r�  c                  C   s�   t �  tdd��I} dd� t�| �D �}d}|D ]1}t�|�}|d7 }ttd|� � � td|� �t	t
�}|�|� |�t�}tt|d j�  � qW d   � d S 1 sTw   Y  d S )	Nr9   r;   c                 S   r<   r=   r>   r?   r>   r>   rB   rC   �  rD   zViewotp.<locals>.<listcomp>r   rE   zGetting Telegram message Otp rG   )rJ   rK   rL   r   r   rM   rN   r  r   rQ   rR   rS   r�   �chatopr  �text)rX   rY   rZ   r[   r\   r]   r�  r>   r>   rB   �Viewotp�  s   


�"�r�  c                  C   �~  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}t|� d�� d
}d
}d
}|D ]g}|d }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� r�|�� j}z|t|�� td|� |� |� d�� |d7 }W q� ty� } zt|� � W Y d }~q�d }~ww q�|d
k�rtd|� d�� td|� d�� ntd|� d�� td|� d�� W d   � d S W d   � d S 1 �s8w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z/ Enterr number accout to join channel or group � send channel/group username z --joining channels--r�  r(  rG   r�  r�  r�  zjoined from: �  Sucesfully-- rE   ra   r�  � Press enter to exit...z Joined succesfully)r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   r*   rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  Zjoin_opr�  r�  r�   r�  r  r�   r�  rM  r>   r>   rB   �groupjoiner�  �p   



���
	�!$�r�  c                  C   r�  )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z0 Enterr number accout to leave channel or group r�  z --Leaving channels--r�  r(  rG   r�  r�  r�  zleft from: r�  rE   ra   r�  r�  z Left succesfully)r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   r   rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  Zleft_opr�  r�  r�   r�  r  r�   r�  rM  r>   r>   rB   �grouplefter�  r�  r�  c                  C   s�  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}d}t|� d|� |� d�� d
}d
}d
}|D ]l}|d }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r	|�� j}z|t|�� td|� d|� |� |� d�� |d7 }W q� t�y } zt|� � W Y d }~q�d }~ww q�|d
k�r td|� d�� td|� d�� ntd|� d�� td|� d�� W d   � d S W d   � d S 1 �sDw   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z* Enter number of accounts to report spam  z% Enter Group,Channel or user usernamerE   z! --Report Spam Started Sucesfullyz account --r�  r(  rG   r�  r�  r�  z=======Reported spam z:from �	======== ra   r�  r�  z all reports done sucessfylly)r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   r   rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  r  r�  r�  r�  r�   r�  r  r�   r�  rM  r>   r>   rB   �
reportspam6	  sr   




���

�#$�r�  c            #   
   C   sB  t j} t j}t j}tj}t�� }|�d� |d d �	� }|�
d�}|d d �	� }ttjt j d|� � � td|� �tt�}|��  |�� r�td�}	|	d	krYttd
 t � n|	dkrvttt� d| � ���}
|tjj|
d��}t�d� g }d }d}g }|t|dt� |dd��}|�|j � |�!� }td�}|d	kr�|D ]}z|j"dkr�|�#|� W q�   Y q�n|dkr�|D ]}z|j$j% W q�   |�#|� Y q�ttd t � d}|D ]}ttd t t|� d d |j& � |d7 }q�td� ttd t �}|t'|� }ttd � t�d� g }|j(|dd�}|�� �r�d}t)j)�*� }|t+dd� }|t+d d� }t,d!d"d#d$�}t-j.|dd%d&�}|�/g d'�� |D ]N}|j0�rT|j0}nd}|j1�r^|j1}nd}|j2�rh|j2} nd} |d( |  �	� }!t3|j%t4��r~|j%j5}"nt6|j%�j7}"|�/|||j8|j9|!|j&|"g� |d }�qJttd) � d S )*Nr�   r�   r�   rf   r�   r�   rG   z:1: Already Joined group Scrape 
2: Join group then Scrape
rQ  z[+] openning scraper�2z Enter Group hashr\  r�   r�   r   r�  zE1: For only public Groups 
2: For all groups public and private both
Tz&[+] Choose a group to scrape members :�[�]r^  rE   ri   z[+] Enter a Number : z[+] Fetching Members...i|  r�   i����r�   i����r�   r:   rc   rd   ra   rg   r�   r�   z![+] Members scraped successfully.):r   r  rP   rU  r   r�   r�   r�   r�   r�   r�   rN   rO   rU   r   rQ   rR   r�   r�   rW   r  r�  rl   r  r   r�  r(   r�   r   r   r   r�  r  Zget_dialogsr   rk   Zentityr�   r�   r�   r  r	   r�   r
   rK   rL   rq   r�   r�   r�   r-  r�   r   r�   r�   r�   r�   r�   )#r;   r�  �br�   r�   r�   r�   r\   r�   �pr  r  r  r	  r
  r  Zdialogsr�   r�  rz   r�  r�  r�   r�   r�   Z	last_weekZ
last_monthrX   rq   r  r�   r�   r-  r�   r�   r>   r>   rB   �
pvtscraperq	  s�   

�
�

��
&




r�  c                  C   s  t �d� tdd��� } | �� }d}d}	 z t|| �}t||d  �}t||d  �}t||d  �}W n   td	� t�	�  Y t
d
| |||d�}|��  |�dt|�� |��  tdt|� d � dd� }	ttd�dd�D ]}
|	�  qr|d7 }|d7 }q)Nr�   zabnumbers.txtr;   rE   r   Tr�   r�   ZFinishedz
Sessionss/)Zphone_numberr  zSession z
 Created !c                   S   s   t d� d S )Ng{�G�z�?r   r>   r>   r>   rB   �process_data�	  s   zantiban.<locals>.process_datar�   z[green]Activating Anti-Ban)�descriptionr�   )r�   r   rK   r�   r�   rl   r�   rN   r�  r�  r   rS   r�   r  r   r�   )ZalfZalf1rz   �jr;  r�  r�   r�   Zappr�  �_r>   r>   rB   �antiban�	  s2   

�r�  c                   C   s�   t �d� t�d� td� t �d� t�d� td� t �d� t�d� td� t �d� t�d� td	� t �d� t�d
� td� td� td� d S )Nr�   zrm -rf SessionsszProcess 1 Donezrm abnumbers.txtzProcess 2 Donezmkdir SessionsszProcess 3 Doneztouch abnumbers.txtzProcess 4 DonezLecho 1 1698327 3a082f726fc9ce0b6b18ff5742ebde20 +19142661153 > abnumbers.txtzProcess 5 DonezAll Process DonezRun script again for main menu)r�   r   rs   r  rN   r>   r>   r>   rB   �	abremover�	  s"   









r�  c                  C   s.   t jD ]} tt� | � d� t j|  � �� qd S )Nz : )rs   �environrN   r  )�itemr>   r>   rB   �getSystemInfo
  s   
 �r�  c                   C   s�  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]|}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r|�� j}z|�|||� td|� |� |� d�� W n t�y } zt|� � W Y d }~q�d }~ww |d
k�r+td|� d�� q�td|� d�� q�W d   � d S 1 �s@w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z$ Enter number of accounts to react  z Enter Group/Channel z Enter Message IDz Enter Reaction rE   � --Sending Reaction from r�  r(  rG   r�  r�  r�  z#=======Successfully added reaction r�  ra   r�  zAll reaction added sucesfully)r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   Zsend_reactionrv  ) r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  �reactionZmsgidZ
reactionopr�  r�  r�  r�   r�  r�   r�  rM  r>   r>   rB   r�  
  sl   
 



��
�$�r�  c            !      C   s�  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]�}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r'|�� j}z|tjj|||d��}t|� � � td|� |� |� d�� W n t!�y& }  zt| � � W Y d } ~ q�d } ~ ww |d
k�r5td|� d�� q�td|� d�� q�W d   � d S 1 �sJw   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z* Enter number of accounts to edit Profile z Enter First Name z Enter Last Namez Enter Bio rE   r�  r�  r(  rG   r�  r�  r�  )r�   r-  Zaboutz)=======Successfully Changed Profile Info r�  ra   r�  �#All profile info changed sucesfully)"r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   r   �accountZUpdateProfileRequest�	stringifyrv  )!r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  Z	firstnameZlastnameZbior�  r�  r�  r�   r�  r�   r�  r  rM  r>   r>   rB   �	profoesitS
  sv   
 


�
��
�$�r�  c                  C   s:  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}|D ]w}t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� r�|�� j}z|tjj|d��}t|� � � td|� |� |� d�� W n t!y� } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �sw   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z Enter Username rE   r�  r�  rG   r�  r�  r�  )r�   z%=======Successfully Changed Username r�  ra   r�  r�  )"r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rl   rW   r   rM   r   rQ   rR   rS   r�   r�  r�   r   r�  �UpdateUsernameRequestr�  rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   Z
usernamedtr�  r�  r�  r�   r�  r  rM  r>   r>   rB   �	usernamec�
  sd   
 

�
��
�$�r�  c                  C   sN  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}|D ]v}t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� r�|�� j}z|tjj||d��}t|� td|� |� |� d�� W n t y� } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z Enter Old Channel Username z Enter New Channel Username rE   z --Changing chnl Username from r�  rG   r�  r�  r�  )rn  r�   z-=======Successfully Changed Channel Username r�  ra   r�  z#Channel username changed sucesfully)!r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rl   rW   r   rM   r   rQ   rR   rS   r�   r�  r�   r   ru  r�  rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   ZuctdZumpcr�  r�  r�  r�   r�  r  rM  r>   r>   rB   �channelusernamec�
  sh   
 

�
��
�$�r�  c                  C   sR  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}|D ]x}t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� r�|�� j}z|tjj||d��}t|� � � td|� |� |� d�� W n t!y� } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s"w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z Enter Channel Username z Enter New Channel Name rE   z --Changing chnl name from r�  rG   r�  r�  r�  )rn  r�   z)=======Successfully Changed Channel name r�  ra   r�  zChannel name changed sucesfully)"r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rl   rW   r   rM   r   rQ   rR   rS   r�   r�  r�   r   ru  ZEditTitleRequestr�  rv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   ZuctdsZumpcsr�  r�  r�  r�   r�  r  rM  r>   r>   rB   �channelnamec	  sh   
 

�
��
�$�r�  c                  C   �`  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]{}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r|�� j}z|j|d� td|� |� |� d�� W n t�y } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s)w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z* Enter number of accounts to edit/set 2FA z Enter New Password rE   z --Editing 2FA from r�  r(  rG   r�  r�  r�  )Znew_passwordz =======Successfully Changed 2FA r�  ra   r�  z!All account 2Fa Edited sucesfully�r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   rl   r   rM   r   rQ   rR   rS   r�   r�  r�   Zedit_2farv  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  Zlovelyr�  r�  r�  r�   r�  r�   r�  rM  r>   r>   rB   �faeditD  �h   
 



��
�$�r�  c                  C   r�  )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z( Enter number of accounts to remove 2FA z Enter Current Password rE   z --Removing 2FA from r�  r(  rG   r�  r�  r�  )Zcurrent_passwordz =======Successfully Removed 2FA r�  ra   r�  z"All account 2Fa Removed sucesfullyr�  )r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  Zpyaarr�  r�  r�  r�   r�  r�   r�  rM  r>   r>   rB   �farm  r�  r�  c                  C   sP  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]~}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� r�|�� j}z|tj�� �}t|� td|� |� |� d�� W n ty� } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s!w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z0 Enter number of accounts to Terminate sessions rE   z' --Terminating All other sessions from r�  r(  rG   r�  r�  r�  z2=======Successfully Terminated All Other Sessions r�  ra   r�  z3All account all other session terminated sucesfully) r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   r   rM   r   rQ   rR   rS   r�   r�  r�   r   ZauthZResetAuthorizationsRequestrv  �r  r�  r;   r:   r  r  r  r�  r�   rw  rx  ry  rz  r{  r\   rX  rA  rY  rZ  r[   r�  r�  r�  r�  r�   r�  r�   r�  r  rM  r>   r>   rB   �trequ�  sh   
 


��
�$�r�  c                  C   sX  t j} t j}t j}t j}t j}t j}t j}||||||g}t�	� }|�
d� |d d }	|d d }
|d d }|d d }|d d }g }tdd	���}t|�}t|�}|D ]}|�t|d
 �� qV|}t|� d|� t|�� �� tt|� d|� ���}d}t|� d|� t|�� |� d�� d
}d
}d
}|D ]�}|d7 }td|� �� t�|�}td|� �tt�}td|� |� |� d|� d�� |��  |�� �r|�� j}z|tj�� �}t|�� � td|� |� |� d�� W n t �y } zt|� � W Y d }~q�d }~ww |d
k�rtd|� d�� q�td|� d�� q�W d   � d S 1 �s%w   Y  d S )Nr�   r�   r�   rf  rg  rh  ri  r9   r;   r   r�  z/ Enter number of accounts to get sessions list rE   z# --Getting All other sessions from r�  r(  rG   r�  r�  r�  z(=======Successfully listed All Sessions r�  ra   r�  z)All account all session listed sucesfully)!r   rU   rU  r  r�  r�  rV   rP   r�   r�   r�   rK   r   rV  rk   r�   rN   rW  rW   r   rM   r   rQ   rR   rS   r�   r�  r�   r   r�  ZGetAuthorizationsRequestr�  rv  r�  r>   r>   rB   �getlis�  sh   
 



��
�$�r�  c               	   C   st	  t �  tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d	�t � tt� dt� dt� d
�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� dt� d�t � tt� dt� dt� d�t � tt� dt� dt� dt� d�t � tt� dt� dt� dt� d�t � tt� dt� dt� d �t � tt� dt� dt� d!�t � tt� dt� dt� d"�t � tt� dt� dt� d#�t � tt� dt� dt� d$�t � tt� dt� dt� d%�t � tt� dt� dt� d&�t � tt� dt� dt� d'�t � tt� dt� dt� d(t� d)�t � tt� dt� dt� d*�t � tt� dt� dt� d+t� d,�t � tt� dt� dt� d-�t � tt� dt� dt� d.t� d/�t � tt� dt� dt� d0t� d/�t � tt� dt� dt� d1�t � tt� dt� dt� d2�t � tt� dt� dt� d3t� d�t � tt� dt� dt� d4t� d�t � tt� dt� dt� d5t� d�t � tt� dt� dt� d6t� d/�t � tt� dt� dt� d7t� d/�t � tt� dt� dt� d8�t � tt� dt� dt� d9�t � tt� dt� dt� d:�t � tt	d;��} | d<k�r(t
�  d S | d=k�r2t�  d S | d>k�r<t�  d S | d?k�rFt�  d S | d@k�rPt�  d S | dAk�rZt�  d S | dBk�rdt�  d S | dCk�rnt�  d S | dDk�rxt�  d S | dEk�r�t�  d S | dFk�r�t�  d S | dGk�r�t�  d S | dHk�r�t�  d S | dIk�r�t�  d S | dJk�r�t�  d S | dKk�r�t�  d S | dLk�r�t�  d S | dMk�r�t�  d S | dNk�r�t�  d S | dOk�r�t�  d S | dPk�r�t�  d S | dQk�r�t�  d S | dRk�rt �  d S | dSk�rt!�  d S | dTk�rt"�  d S | dUk�r"t#�  d S | dVk�r,t$�  d S | dWk�r6t%�  d S | dXk�r@t&�  d S | dYk�rJt'�  d S | dZk�rTt(�  d S | d[k�r^t)�  d S | d\k�rht*�  d S | d]k�rrt+�  d S | d^k�r|t,�  d S | d_k�r�t-�  d S | d`k�r�t.�  d S | dak�r�t/�  d S | dbk�r�t0�  d S | dck�r�t1�  d S | ddk�r�t2�  d S d S )eNz[+]    z
CHOOSE    z[A]  -|||   Account Option:z[1]   >>>   Loginz[2]   >>>   Banfilter + removerz$[3]   >>>   spambotchecker + removerz'[B]  -|||   Advanced Scraper & Filters:z[4]   >>>   Scraper z[5]   >>>   Private Scraper z[6]   >>>   Daily Filter z[7]   >>>   Weekly Filter z[8]   >>>   Scrap Admin z[9]   >>>   Monthly Filter z[10]  >>>   NonActive Filter z![11]  >>>   Deletealreadynumbers z[C]  -|||   Profile Pic Change:z[12]  >>>   Set profile Picz[13]  >>>   Delete profile Picz![D]  -|||   Contact Adder Option:z[14]  >>>   Autoaddcontact - z	For Phonez[15]  >>>   Deletecontact  z$[E]  -|||   Additional Adder optionsz[16]  >>>   Bulk Adderz[17]  >>>   SingleAdderz[18]  >>>   Username Adder - �Singlez[19]  >>>   SingleJoinedAdderz[20]  >>>   Adder - ZRecommendedz[21]  >>>   User ID Adder - z[22]  >>>   Multiple adderz[F]  -|||   ExtraFeatures:z[23]  >>>   Join Group/Channelz[24]  >>>   Leave Group/Channelz[G]  -|||   Additional Options:z[25]  >>>   Telegram OTP viewerz[26]  >>>   Send Messagez[27]  >>>   Report Spam A Userz[28]  >>>   Scam Tag - ZUpdatedz[H]  -|||   AntiBan Tools:z [29]  >>>   Antiban Activator - ZImprovedz'[30]  >>>   Antiban All Account Removerz[31]  >>>   Get System Info - ZNewz![32]  >>>   Reaction Increaser - z[I]  -|||   Settings Option:z*[33]  >>>   Edit First, Last Name and Bio z"[34]  >>>   Change acc Username - z#[35]  >>>   Change chnl Username - z[36]  >>>   Change chnl Name - z[37]  >>>   Edit/Set 2FA - z[38]  >>>   Remove 2FA - z([39]  >>>   Terminate all other Sessionsz[40]  >>>   See all Sessionsz[41]  >>>   Exitz
Enter your choice: rE   r�   r�   r�   r�   r�   r�   �   �	   rs  �   �   �   �   �   �   �   �   �   r�  �   �   �   �   �   �   �   �   �   r�   �   �    �!   �"   �#   �$   �%   �&   �'   r�  �)   )3rJ   rN   r  r  r  r  r;   r!  r�   rW   r_   r�   r�   r�   r�  r�   r�   r�   r�   r�   r  r  r  r[  re  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  rR  )r;  r>   r>   rB   �	main_menu0  s  $$$$$$$$$$$$$

















































































�r  )�r�  Zrequestsr�   rs   r�  r5  r�  r�   r  r_  rL   Zjsonr�   Zrich.progressr   Zpyrogramr   r   ZIP2Locationr   r�  r  Zpytzr   r	   r   r
   r   r   r   r   Ztelethon.syncr   r   r   r   r   r   r   Ztelethon.tl.functions.channelsr   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.typesr   r   r   r   r   r   r   r    r!   r"   r#   r$   Ztelethon.tl.functions.contactsr%   r&   Ztelethon.tl.functions.photosr'   r(   r)   r*   r+   Ztelethon.errorsr,   Ztelethon.errors.rpcerrorlistr-   r.   r/   r0   r1   r2   r3   r4   Ztelethon.sessionsr5   r�  rQ   rR   r�  r  r  ZwirN   �get�versionr�  �floatr�  rl   rW   �promptr�   r  �path�exists�mkdirrK   r_   r�   r�   r�   r�   r�   r�   r�   r�   r  r  r  rU   r  ZLIGHTGREEN_EXr�  r  r;   r�  r:   r�  rV   r  rU  r!  r�  rJ   r[  re  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r  r>   r>   r>   rB   �<module>   s�   h $8(








v3?@-@F  (YF /w<a  V  ::;k#=B9;;;;;; 
